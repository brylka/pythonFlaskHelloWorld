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
                script {
                    // Logowanie przed uruchomieniem aplikacji
                    echo 'Uruchamianie aplikacji Flask...'
                    // Uruchamianie aplikacji Flask
                    bat 'venv\\Scripts\\activate && start /B python app.py > output.log 2>&1'
                    // Sprawdzenie, czy aplikacja działa
                    bat 'timeout /T 5'
                    bat 'type output.log'
                }
            }
        }
    }
}
