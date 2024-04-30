pipeline{
    agent any
    stages {
        stage('Dev - Deployment'){
            steps {
                sh 'sudo su'
                sh 'ssh -i /var/lib/jenkins/workspace/Jenkin.pem ubuntu@ec2-3-144-180-19.us-east-2.compute.amazonaws.com "rm -rf /home/ubuntu/Mental-health-assistance && git clone https://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@github.com/invika/Mental-health-assistance.git"'
                sh 'ssh -i /var/lib/jenkins/workspace/Jenkin.pem ubuntu@ec2-3-144-180-19.us-east-2.compute.amazonaws.com "cd /home/ubuntu/Mental-health-assistance/ && sudo chmod -R 777 /home/ubuntu/Mental-health-assistance/Jenkins/ && /home/ubuntu/Mental-health-assistance/Jenkins/app_setup.sh > app_setup.log && /home/ubuntu/Mental-health-assistance/Jenkins/env_setup.sh > env_setup.log && /home/ubuntu/Mental-health-assistance/Jenkins/app_start.sh > app_start.log" &'
            }
        }
    }
}