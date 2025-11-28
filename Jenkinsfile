pipeline {
    agent any

    environment {
        PA_TOKEN = credentials('PA_API_TOKEN') // use the ID from above
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/sagar-kamankar/djago_project.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && python manage.py test'
            }
        }

        stage('Deploy to PythonAnywhere') {
            steps {
                sh """
                . venv/bin/activate
                pa_autoconfigure_django.py \\
                --api-token=$PA_TOKEN \\
                --domain=yourusername.pythonanywhere.com \\
                --project-root=/home/yourusername/djago_project
                """
            }
        }
    }
}
