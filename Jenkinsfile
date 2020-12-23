def network='jenkins-${BUILD_NUMBER}'

pipeline {
  
   agent any

   stages{
      stage('Create Network') {
         steps{
            sh "docker network create ${network}"
         }
      }
      stage('Install docker-compose') {
        steps {
          sh "pip install docker-compose"
        }
      }
      stage('Build') {
        steps {
          sh "docker-compose build"
        }
      }
      stage('Run Test') {
         steps{
            sh "docker-compose start selenium && docker-compose run django"
         }
      }
    }
    post{
      always {
         sh "docker network rm ${network} && docker-compose stop selenium"
      }   
   }
}