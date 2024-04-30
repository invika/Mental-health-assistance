pipeline{
    agent any
    stages {
        // stage('Cleanup Workspace') {
            // steps {
                // cleanWs() // Cleanup workspace
            // }
        // }
        stage('Setup the Application'){
            steps {
                sh '''
                chmod +x ./Jenkins/app_setup.sh
                ./Jenkins/app_setup.sh
                '''
            }
        }
        stage('Setup Python Virtual ENV for dependencies'){
            steps  {
                sh '''
                chmod +x ./Jenkins/env_setup.sh
                ./Jenkins/env_setup.sh
                '''}
            post {
                always {
                    input 'Deploy the Application on server?'
                }
            }
        }
        stage('Start the Application'){
            steps {
                sh '''
                sudo ufw enable
                sudo ufw reload
                sudo ufw status
                ls
                chmod +x ./Jenkins/app_start.sh
                ./Jenkins/app_start.sh
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