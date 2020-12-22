pipeline {
     environment {
          registry = "jinyunglim/smsbackend"
          registryCredential = 'dockerhub_id'
          dockerImage= ''
     }
    agent any
    stages {
        stage('Test') {
             agent {
                  docker {
                       image 'qnib/pytest'
                  }
             }
             steps {
                  sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python helloworld/sms/tests.py'
             }
        }
        stage('Build Docker image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            } 
        }
        stage('Deploy Docker image') {
             steps{
                  script{
                       docker.withRegistry('', registryCredential){
                            dockerImage.push()
                       }
                  }
             }
        }

        stage('Cleaning up docker') {
             steps {
                  sh 'docker rmi $registry:$BUILD_NUMBER'
             }
        }
    }
    post {
         always {
              emailext body: 'A Test Email', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
         }
    }
}