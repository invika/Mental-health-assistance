from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import CustomUser
from .models import Doctor
from .models import Emotions
import time
from collections import Counter


import cv2
from keras.models import model_from_json
import numpy as np

from django.http import StreamingHttpResponse
from django.views.decorators import gzip

def index(request):
    return render(request, "home/index.html", {})

# Create your views here.
@never_cache
def login(request):
    return render(request, "home/loginpage.html", {})

@require_POST
def validate_login(request):
    try:
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
    except Exception as e:
        messages.error(request, "Username is already in use.")
        return redirect("home/loginpage.html")
        
    if user is not None:
        auth_login(request, user)
        customuser = CustomUser.objects.get(email=request.POST.get("username"))  
        request.session['city'] = customuser.city
        request.session['username'] = customuser.email
        request.session['goal'] = customuser.goal
        return redirect("home")
    else:
        messages.error(request, "Username/Password incorrect.")
        return render(request, 'home/loginpage.html', {})
##error rectified login details
@never_cache
def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("re_password") 
        goal = request.POST.get("goal")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        mobile = str(request.POST.get("mobile"))
        address = request.POST.get("address")
        city = request.POST.get("city")
        date_of_birth = request.POST.get("dob")
        horror = bool(request.POST.get("horror"))
        action = bool(request.POST.get("action"))
        sciencefiction = bool(request.POST.get("sciencefiction"))
        thriller = bool(request.POST.get("thriller"))
        comedy = bool(request.POST.get("comedy"))
        romance = bool(request.POST.get("romance"))
        favourite_sports_and_places = request.POST.get("favourite_sports_and_places")
        interests = request.POST.get("intrests") 
        username = email

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already in use.")
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address is already registered.")
            return redirect("register")
        
        user = User.objects.create_user(username=username, password=password)
        custom_user = CustomUser.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            address=address,
            goal=goal,
            city=city,
            date_of_birth=date_of_birth,
            horror=horror,
            email=email,
            mobile=mobile,
            action=action,
            science_fiction=sciencefiction,
            thriller=thriller,
            comedy=comedy,
            romance=romance,
            favourite_sports_and_places=favourite_sports_and_places,
            intrests=interests
        )

        authenticated_user = authenticate(request, username=username, password=password)
        auth_login(request, authenticated_user)  
        return redirect("home")
    
    return render(request, "home/register.html", {})
##updated some entries
@login_required
@never_cache
def home(request):
    return render(request, "customer/index.html", {"custom": CustomUser.objects.get(user=request.user)})

def edituser(request, id):  
    userob = CustomUser.objects.get(id=id)
    print("firstname=" , userob.user.password)  
    return render(request,'edituser.html', {'userob':userob})  

@require_POST
def updateuser(request):
    print('===' * 20)
    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        mobile = str(request.POST.get("mobile"))
        address = request.POST.get("address")
        date_of_birth = request.POST.get("dob")
        horror = bool(request.POST.get("horror"))
        action = bool(request.POST.get("action"))
        sciencefiction = bool(request.POST.get("sciencefiction"))
        thriller = bool(request.POST.get("thriller"))
        comedy = bool(request.POST.get("comedy"))
        romance = bool(request.POST.get("romance"))
        favourite_sports_and_places = request.POST.get("favourite_sports_and_places")
        interests = request.POST.get("intrests") 
        
        user = CustomUser.objects.get(email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.mobile = mobile
        user.address = address
        user.date_of_birth = date_of_birth
        user.horror = horror
        user.action = action
        user.science_fiction = sciencefiction
        user.thriller = thriller
        user.comedy = comedy
        user.romance = romance
        user.favourite_sports_and_places = favourite_sports_and_places
        user.intrests = interests
        # Save the updated user object
        user.save()
        return redirect("home")
    
    return redirect("edituser")


def assistant(request):
    return render(request, "customer/assistant.html", {})

##############
################
def most_common_item(lst):
    counts = Counter(lst)
    most_common = counts.most_common(1)
    return most_common[0][0] if most_common else None

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1,48,48,1)
    return feature/255.0

def generate(request):
    json_file = open("myapp/assitantmodal/facialemotionmodel.json", "r")
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)

    model.load_weights("myapp/assitantmodal/facialemotionmodel.h5")
    haar_file=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade=cv2.CascadeClassifier(haar_file)


    # Set up camera
    webcam = cv2.VideoCapture(0)
    labels = {0 : 'angry', 1 : 'disgust', 2 : 'fear', 3 : 'happy', 4 : 'neutral', 5 : 'sad', 6 : 'surprise'}
    predictionArray = []
    start_time = time.time()
    while (time.time() - start_time) < 8:
        i,im=webcam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(im,1.3,5)
        try: 
            for (p,q,r,s) in faces:
                image = gray[q:q+s,p:p+r]
                cv2.rectangle(im,(p,q),(p+r,q+s),(255,0,0),2)
                image = cv2.resize(image,(48,48))
                img = extract_features(image)
                pred = model.predict(img)
                prediction_label = labels[pred.argmax()]
                # print("Predicted Output:", prediction_label)
                # cv2.putText(im,prediction_label)
                predictionArray.append(prediction_label)
                cv2.putText(im, '% s' %(prediction_label), (p-10, q-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2, (0,0,255))
                
            #cv2.imshow("Output",im)
            # Convert frame to JPEG
            ret, buffer = cv2.imencode('.jpg', im)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

            # cv2.waitKey(27)
        except cv2.error:
            pass
    try:
        most_occurred = most_common_item(predictionArray)
        print("predicted Array:",most_occurred)
        emotion = Emotions.objects.create(
                username=request.session['username'],
                emotionname=most_occurred
            )
        emotion.save()
        show_modal = True  # Set this to True or False based on your conditions
        return redirect(request, '/index/')
    except Exception as e:
        print("Error:", e)

    

@gzip.gzip_page
def video_feed(request):
    return StreamingHttpResponse(generate(request), content_type='multipart/x-mixed-replace; boundary=frame')


def healthreference(request):
    return render(request, "customer/healthreference.html", {})


def nearbydoctors(request):
    doctors = None
    try:
        city = request.session.get('city')
        if city:
            doctors = Doctor.objects.filter(city=city)
    except:
        pass
    return render(request, "customer/nearbydoctors.html", {'doctors': doctors})

def history(request):
    history = None
    userEmotions = []
    goal=""
    try:
        username = request.session['username']
        if username:
            history = Emotions.objects.filter(username=username)
            for row in history:
                userEmotions.append(row.emotionname)
            goal = most_common_item(userEmotions)
        print("Goal",goal,username)
    except Exception as e:
        print("Error:", e)
    return render(request, "customer/history.html", {'history': history,'goal':goal})
