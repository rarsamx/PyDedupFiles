/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh '''
                    echo "This is the second step"
                    ls -lah
                '''
            }
        }
    }
}
