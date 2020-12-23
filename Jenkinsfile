// def network='jenkins-${BUILD_NUMBER}'

pipeline {
  
   agent any

   stages{
      // stage('Create Network') {
      //    steps{
      //       sh "docker network create ${network}"
      //    }
      // }
      stage("Install doocker-compose") {
        steps{
          sh "curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"
        }
      }
      stage('Build') {
        steps {
          withEnv(["PATH=$PATH:/docker-compose"]){
            sh "docker-compose up -d"
            sh "docker-compose build"
          }
          // sh "docker-compose build"
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