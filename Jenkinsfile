def network='jenkins-${BUILD_NUMBER}'

pipeline {
  
   agent any

   stages{
      stage('Setting Up') {
         steps{
            sh "docker network create ${network} && /usr/local/bin/docker-compose up --build"
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