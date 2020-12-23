//variables
def network='jenkins-${BUILD_NUMBER}'
def seleniumHub='selenium-hub-${BUILD_NUMBER}'
def chrome='chrome-${BUILD_NUMBER}'
pipeline {
  
   agent { label 'docker' }

   stages{
      stage('Setting Up Selenium Grid') {
         steps{        
            sh "docker network create ${network}"
            sh "docker run -d -p 4444:4444 --name ${seleniumHub} --network ${network} selenium/hub"
            sh "docker run -d -e HUB_PORT_4444_TCP_ADDR=${seleniumHub} -e HUB_PORT_4444_TCP_PORT=4444 --network ${network} --name ${chrome} selenium/node-chrome"
         }
      }
      stage('Run Test') {
         steps{
            sh "docker-compose build && docker-compose start selenium && docker-compose run django"
         }
      }
    }
    post{
      always {
         sh "docker rm -vf ${chrome}"
         sh "docker rm -vf ${seleniumHub}"
         sh "docker network rm ${network}"
      }   
   }
}