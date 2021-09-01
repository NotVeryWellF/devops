pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh '''apt-get update
                      apt-get install python, python-pip
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