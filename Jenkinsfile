def network='jenkins-${BUILD_NUMBER}'

pipeline {
  
   agent any

   stages{
      stage('Setting Up') {
         steps{
            sh "docker network create ${network} && curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"
         }
      }
      stage('Build') {
        steps {
          sh 'docker-compose build'
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