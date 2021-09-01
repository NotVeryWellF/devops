pipeline {
    agent { docker { image 'python:3.9-slim-buster' } }
    stages {
        stage('build') {
            steps {
                sh '''
                      pip install --upgrade pip
                      pip install -r ./app_python/requirements.txt
                   '''

            }
        }
        stage('test') {
            steps {
                sh "python -m pytest ./app_python/tests/test.py"
            }
        }
    }
}