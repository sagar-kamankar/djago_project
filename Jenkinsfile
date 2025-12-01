pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/sagar-kamankar/djago_project.git'
            }
        }

        stage('Deploy to PythonAnywhere') {
            steps {
                withCredentials([string(credentialsId: 'PA_API_TOKEN', variable: 'PA_TOKEN')]) {
                    sh '''
                    echo "Zipping project..."
                    zip -r project.zip .

                    echo "Uploading project to PythonAnywhere..."
                    curl -X POST "https://www.pythonanywhere.com/api/v0/user/hackersaggyhacker/files/path/home/hackersaggyhacker/project.zip" \
                        -H "Authorization: Token $PA_TOKEN" \
                        --form "content=@project.zip"

                    echo "Extracting project on PythonAnywhere..."
                    curl -X POST "https://www.pythonanywhere.com/api/v0/user/hackersaggyhacker/consoles/python3.10/run/" \
                        -H "Authorization: Token $PA_TOKEN" \
                        --data "command=unzip -o /home/hackersaggyhacker/project.zip -d /home/hackersaggyhacker/djago_project/"
                    
                    echo "Reloading Web App..."
                    curl -X POST "https://www.pythonanywhere.com/api/v0/user/hackersaggyhacker/webapps/hackersaggyhacker.pythonanywhere.com/reload/" \
                        -H "Authorization: Token $PA_TOKEN"
                    '''
                }
            }
        }
    }
}
