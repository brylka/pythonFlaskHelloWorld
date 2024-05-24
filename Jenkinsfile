pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    if (fileExists('venv')) {
                        sh 'rm -rf venv'
                    }
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                sh 'source venv/bin/activate && pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'source venv/bin/activate && nohup python app.py &'
            }
        }
    }
}
