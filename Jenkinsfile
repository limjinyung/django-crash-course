 /* This pipeline creates a docker compose and then executes all the scripts. Note the Jenkins has to be in Linux environment */
node {
    stage('Clone repository') {
        /* Clone repository */
        checkout scm
    }

    stage('Docker Setup') {
        parallel(
          "Start Compose": {
    		/* Start docker-compose with five instances of Chrome */
    	    cmd_exec('docker-compose up -d --scale chrome=5 --scale firefox=0')
          },
          "Build Image": {
            /* This builds an image with all pytest selenium scripts in it */
    		def dockerfile = 'Dockerfile'
            app = docker.build("pytest-with-src","-f ${dockerfile} ./")
          }
        )
    }    


}

