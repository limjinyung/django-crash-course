def network='jenkins-${BUILD_NUMBER}'

pipeline {
  
   agent any

   stages{
      stage('Create Network') {
         steps{
            sh "docker network create ${network}"
         }
      }
      // stage('Give permission') {
      //   steps {
      //     sh "docker exec -u root -it d2cadeec104d bin/bash && chown jenkins:docker /var/run/docker.sock"
      //   }
      // }
      stage('Install docker-compose') {
        steps {
          sh "curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` \
    >~/docker-compose && chmod +x ~/docker-compose && sudo mv ~/docker-compose /usr/local/bin/docker-compose"
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