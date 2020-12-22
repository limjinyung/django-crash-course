pipeline {
    agent any
    stages {
        stage('Test') {
             agent {
                  docker {
                       image 'python:3.6'
                  }
             }
             steps {
                  sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python3.6 sms/tests.py'
             }
        }
    }
    post {
         always {
              emailext body: 'A Test Email', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
         }
    }
}