pipeline{
    agent any
    stages {
        stage('Dev - Deployment'){
            steps {
                sh 'sudo su'
                //sh 'scp -i /var/lib/jenkins/workspace/Jenkin.pem -o StrictHostKeyChecking=no -r ../Mental-Health-Assistance ubuntu@ec2-3-144-180-19.us-east-2.compute.amazonaws.com:~'
                sh 'ssh -i /var/lib/jenkins/workspace/Jenkin.pem ubuntu@ec2-3-144-180-19.us-east-2.compute.amazonaws.com "git clone https://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@github.com/invika/Mental-health-assistance.git"'
                sh 'ssh -i /var/lib/jenkins/workspace/Jenkin.pem ubuntu@ec2-3-144-180-19.us-east-2.compute.amazonaws.com "cd ~/Mental-Health-Assistance/ && sudo chmod -R 777 ./Jenkins/ && ./Jenkins/app_setup.sh > deployment1.log  && ./Jenkins/app_start.sh > deployment2.log && ./Jenkins/env_setup.sh > deployment3.log"'
            }
            post {
                always {
                    input 'Deploy to Testing?' // Wait for user input to proceed to testing deployment
                }
            }

        }
        stage('Test - Deployment'){
            steps {
                sh 'sudo su'
                //sh 'scp -i "/var/lib/jenkins/workspace/Jenkin.pem" -o StrictHostKeyChecking=no -r ../Mental-Health-Assistance ubuntu@ec2-3-135-104-190.us-east-2.compute.amazonaws.com:~'
                sh 'ssh -i /var/lib/jenkins/workspace/Jenkin.pem ubuntu@ec2-3-144-180-19.us-east-2.compute.amazonaws.com "git clone https://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@github.com/invika/Mental-health-assistance.git ~/"'
                sh 'ssh -i "/var/lib/jenkins/workspace/Jenkin.pem" ubuntu@ec2-3-135-104-190.us-east-2.compute.amazonaws.com "cd ~/Mental-Health-Assistance/ && sudo chmod -R 777 ./Jenkins/ && ./Jenkins/app_setup.sh > deployment1.log && ./Jenkins/app_start.sh > deployment2.log && ./Jenkins/env_setup.sh > deployment3.log"'
            }
            post {
                always {
                    input 'Deploy to Production?' // Wait for user input to proceed to production deployment
                }
            }
        }
        stage('Prod - Deployment'){
            steps {
                sh 'sudo su'
                sh 'scp -i "/var/lib/jenkins/workspace/Jenkin.pem" -o StrictHostKeyChecking=no -r Mental-Health-Assistance ubuntu@ec2-3-138-62-178.us-east-2.compute.amazonaws.com:~'
                sh 'ssh -i "/var/lib/jenkins/workspace/Jenkin.pem" ubuntu@ec2-3-138-62-178.us-east-2.compute.amazonaws.com "cd ~/Mental-Health-Assistance/ && sudo chmod -R 777 ./Jenkins/ && ./Jenkins/app_setup.sh > deployment1.log && ./Jenkins/app_start.sh > deployment2.log && ./Jenkins/env_setup.sh > deployment3.log"'
            }
        }
    }
}