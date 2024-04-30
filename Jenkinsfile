pipeline{
    agent any
    stages {
        stage('Cleanup Workspace') {
            steps {
                cleanWs() // Cleanup workspace
            }
        }
         stage('Checkout from Git') {
            steps {
              script {
                    withCredentials([string(credentialsId: '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', variable: 'PAT')]) {
                        git branch: 'main', credentialsId: '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', url: 'https://github.com/invika/Mental-health-assistance.git'
                    }
                }
            }
        }
        stage('Dev - Deployment'){
            steps {
                sh '''
                ssh -i "/var/lib/jenkins/workspace/Jenkin.pem" "cd /var/lib/jenkins/workspace/Mental-Health-Assistance/ && sudo chmod -R 777 ./Jenkins/ && ./Jenkins/app_setup.sh && ./Jenkins/app_start.sh && ./Jenkins/env_setup.sh"
                '''
            }
            post {
                always {
                    input 'Deploy to Testing?' // Wait for user input to proceed to testing deployment
                }
            }

        }
        stage('Test - Deployment'){
            steps {
                sh '''
                ssh -i "/var/lib/jenkins/workspace/Jenkin.pem" "cd /var/lib/jenkins/workspace/Mental-Health-Assistance/ && sudo chmod -R 777
                '''
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
                ssh -i "/var/lib/jenkins/workspace/Jenkin.pem" "cd /var/lib/jenkins/workspace/Mental-Health-Assistance/ && sudo chmod -R 777
                '''
        }
    }
        stage('Ping URL and Exit from Pipeline') {
            steps {
                script {
                    def startTime = currentBuild.startTimeInMillis
                    def endTime = startTime + (5 * 60 * 1000) // 5 minutes timeout
                    def pingExitStatus = -1

                    // Loop until ping is successful or timeout is reached
                    while (System.currentTimeMillis() < endTime && pingExitStatus != 0) {
                        pingExitStatus = sh(script: 'nc -zv 13.201.9.131 8000', returnStatus: true)
                        if (pingExitStatus == 0) {
                            echo 'Ping successful. Continuing with pipeline.'
                            break
                        }
                        sleep 10 // Sleep for 10 seconds before trying again
                    }

                    // If ping was not successful within timeout period
                    if (pingExitStatus != 0) {
                        error 'Failed to ping URL within 5 minutes timeout.'
                    }
                }
            }
        }
    }
}