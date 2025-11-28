pipeline {
    agent any

    environment {
        PA_USERNAME = "hackersaggyhacker"
        PA_TOKEN = credentials('16c8c2ed749969371535bf125ea357ed798f0b7c')
        APP_NAME = "hackersaggyhacker.pythonanywhere.com"
    }

    stages {
        stage('Pull Code') {
            steps {
                echo "Pulling latest code from GitHub..."
            }
        }

        stage('Deploy to PythonAnywhere') {
            steps {
                echo "Uploading project to PythonAnywhere..."

                sh '''
                    curl -X POST \
                    -H "Authorization: Token ${PA_TOKEN}" \
                    https://www.pythonanywhere.com/api/v0/user/${PA_USERNAME}/webapps/${PA_USERNAME}.pythonanywhere.com/reload/
                '''
            }
        }
    }
}
