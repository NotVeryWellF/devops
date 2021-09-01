pipeline {
    agent { docker { image 'python:3.8.0-slim-buster' } }
    stages {
        stage('dependencies') {
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
        stage('build') {
            steps {
                sh '''
                   cd ./app_python
                   docker build -t webapp .
                   '''
            }
        }
    }
}