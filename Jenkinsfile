pipeline {
    agent any
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