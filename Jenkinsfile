pipeline {
    agent { docker { image 'python:3.9-slim-buster' } }
    stages {
        stage('build') {
            steps {
                sh "echo hello_world"
            }
        }
        stage('test') {
            steps {
                sh "python -m pytest ./app_python/tests/test.py"
            }
        }
    }
}