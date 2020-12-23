 /* This pipeline creates a docker compose and then executes all the scripts. Note the Jenkins has to be in Linux environment */
node {

    stage('Clone repository') {
        /* Clone repository */
        checkout scm
    }

    stage('Build') {
        steps {
          sh "docker-compose build"
        }
    }

    stage('Start Selenium') {
      steps {
        sh "docker-compose start selenium"
      }
    }

    stage('Run Test') {
      steps {
        sh "docker-compose run django"
      }
    }


}

