pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    if (fileExists('venv')) {
                        bat 'rmdir /S /Q venv'
                    }
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def workspace = env.WORKSPACE
                    bat 'venv\\Scripts\\activate && set PYTHONPATH=%workspace% && pytest'
                }
            }
        }
        stage('Deploy') {
            steps {
                bat 'venv\\Scripts\\activate && python app.py'
            }
        }
    }
}
