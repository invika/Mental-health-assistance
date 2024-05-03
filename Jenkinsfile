pipeline{
    agent any
    stages {
        stage('Dev - Deployment'){
            steps {
                sh 'sudo su'
                sh 'ssh -i /var/lib/jenkins/workspace/project.pem -o StrictHostKeyChecking=no ubuntu@ec2-18-216-205-169.us-east-2.compute.amazonaws.com "rm -rf /home/ubuntu/Mental-health-assistance && git clone https://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@github.com/invika/Mental-health-assistance.git"'
                sh 'ssh -i /var/lib/jenkins/workspace/project.pem -o StrictHostKeyChecking=no ubuntu@ec2-18-216-205-169.us-east-2.compute.amazonaws.com "cd /home/ubuntu/Mental-health-assistance/ && sudo chmod -R 777 /home/ubuntu/Mental-health-assistance/Jenkins/ && /home/ubuntu/Mental-health-assistance/Jenkins/app_setup.sh > app_setup.log && /home/ubuntu/Mental-health-assistance/Jenkins/env_setup.sh > env_setup.log && JENKINS_NODE_COOKIE=dontKillMe nohup /home/ubuntu/Mental-health-assistance/Jenkins/app_start.sh > app_start.log &"'
            }
        }
    }
}