pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip wheel setuptools'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && pip install pytest'
                sh '. venv/bin/activate && pytest -v'
            }
        }

        stage('Build') {
            steps {
                sh '. venv/bin/activate && python setup.py sdist bdist_wheel'
                archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}