pipeline{
    agent any
    stages {
        stage('Cleanup Workspace') {
            steps {
                cleanWs() //Cleanup workspace
            }
        }
        stage('Dev - Deployment'){
            steps {
                sh 'pwd'
                sh 'ssh-keyscan -H ec2-3-144-180-19.us-east-2.compute.amazonaws.com >> ~/.ssh/known_hosts'
                sh 'scp -i "/var/lib/jenkins/workspace/Jenkin.pem" -r ../Mental-Health-Assistance ubuntu@ec2-3-144-180-19.us-east-2.compute.amazonaws.com:~'
                sh 'ssh -i "/var/lib/jenkins/workspace/Jenkin.pem" ubuntu@ec2-3-144-180-19.us-east-2.compute.amazonaws.com "cd ~/Mental-Health-Assistance/ && sudo chmod -R 777 ./Jenkins/ && ./Jenkins/app_setup.sh > deployment.log  && ./Jenkins/app_start.sh > deployment.log && ./Jenkins/env_setup.sh > deployment.log"'
            }
            post {
                always {
                    input 'Deploy to Testing?' // Wait for user input to proceed to testing deployment
                }
            }

        }
        stage('Test - Deployment'){
            steps {
                sh 'pwd'
                sh 'scp -i "/var/lib/jenkins/workspace/Jenkin.pem" -r ../Mental-Health-Assistance ubuntu@ec2-3-135-104-190.us-east-2.compute.amazonaws.com:~'
                sh 'ssh -i "/var/lib/jenkins/workspace/Jenkin.pem" ubuntu@ec2-3-135-104-190.us-east-2.compute.amazonaws.com "cd ~/Mental-Health-Assistance/ && sudo chmod -R 777 ./Jenkins/ && ./Jenkins/app_setup.sh > deployment.log && ./Jenkins/app_start.sh > deployment.log && ./Jenkins/env_setup.sh > deployment.log"'
            }
            post {
                always {
                    input 'Deploy to Production?' // Wait for user input to proceed to production deployment
                }
            }
        }
        stage('Prod - Deployment'){
            steps {
                sh '''
                touch deployment.log
                scp -i "/var/lib/jenkins/workspace/Jenkin.pem" -r Mental-Health-Assistance ubuntu@ec2-3-138-62-178.us-east-2.compute.amazonaws.com:~
                ssh -i "/var/lib/jenkins/workspace/Jenkin.pem" ubuntu@ec2-3-138-62-178.us-east-2.compute.amazonaws.com "cd ~/Mental-Health-Assistance/ && sudo chmod -R 777 ./Jenkins/ && ./Jenkins/app_setup.sh > deployment.log && ./Jenkins/app_start.sh > deployment.log && ./Jenkins/env_setup.sh > deployment.log"
                '''
            }
        }
    }
}