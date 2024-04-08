



from django.urls import path
from .views import home, login, validate_login, register, edituser, updateuser, assistant, video_feed, healthreference, nearbydoctors
from  django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', login, name="login"),
    path('validate_login', validate_login, name="validate_login"),
    path('register', register, name="register"),
    path('home', home, name="home"),
    path('edituser/<int:id>', edituser, name="edituser"),
    path('updateuser', updateuser, name="updateuser"),
    path('logout/', LogoutView.as_view(), name="logout"),
     path('assistant', assistant, name="assistant"),
     path('video_feed/', video_feed, name='video_feed'),
     path('healthreference/', healthreference, name='healthreference'),
      path('nearbydoctors/', nearbydoctors, name='nearbydoctors')

]




