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
          sh "curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh && curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose"
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