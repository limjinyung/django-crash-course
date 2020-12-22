pipeline {
    agent any
    stages {
        stage('Test') {
             agent {
                  docker {
                       image 'qnib/pytest && python:3.6.1-alpine'
                  }
             }
             steps {
                  sh 'python3 --version'
                  sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python sms/tests.py'
             }
        }
    }
    post {
         always {
              emailext body: 'A Test Email', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
         }
    }
}