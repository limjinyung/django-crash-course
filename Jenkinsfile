def network='jenkins-${BUILD_NUMBER}'

pipeline {

  environment {
    PATH = "$PATH:/Program Files/Docker/Docker/resources/bin/docker-compose.exe"
  }
  
   agent any

   stages{
      stage('Create Network') {
         steps{
            sh "docker network create ${network}"
         }
      }
      stage("Print ENV") {
        steps {
          sh 'printenv'
        }
      }
      stage('Install docker-compose') {
        steps {
          sh "rm /usr/local/bin/docker-compose"
          sh "curl -fsSL get.docker.com -o get-docker.sh"
          sh "sh get-docker.sh"
          sh "curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose"
          sh "chmod +x /usr/local/bin/docker-compose"
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