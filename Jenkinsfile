/* Requires the Docker Pipeline plugin */
pipeline {
    agent none
/*
    options { 
        timeout(time: 60, unit: 'SECONDS')
    }
*/
/*    agent { docker { image 'python:3.10.7-alpine' } } */
/*    agent { docker { image 'python:3' } }*/

    stages {
/*
        stage('Check python') {
            
            agent { docker { image 'python:3.10.7-alpine' } } 
            steps {
                sh 'python --version'
            }
        }
*/      
        stage('Find dups') {
            agent { docker { image 'python:3' } }
            steps {
                sh '''
                    echo "This is the second step"
                    hostname
                    which identify
                    ls -lR
                    chmod +x findDuplicateImages.sh
                    echo "nothing" > test1.jpg
                    echo "nothing" > test2.jpg
                    ./findDuplicateImages.sh ./
                '''
            }
        }

    }
}
