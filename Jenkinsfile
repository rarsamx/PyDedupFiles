/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'dnf install imagemagick'
                sh '''
                    echo "This is the second step"
                    chmod +x findDuplicateImages.sh
                    echo "nothing" > test1.jpg
                    echo "nothing" > test2.jpg
                    ./findDuplicateImages.sh ./test
                '''
            }
        }
    }
}
