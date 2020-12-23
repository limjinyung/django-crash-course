def network='jenkins-${BUILD_NUMBER}'

pipeline {
  
   agent any

   stages{
      stage('Create Network') {
         steps{
            sh "docker network create ${network}"
         }
      }
      stage('Give permission') {
        steps {
          sh "docker exec -u root -it d2cadeec104d bin/bash"
        }
      }
      stage('Install docker-compose') {
        steps {
          sh "apt-get install python-pip && pip install docker-compose"
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