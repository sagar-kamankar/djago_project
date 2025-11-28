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

                    echo "Uploading ZIP to PythonAnywhere..."
                    curl -X POST "https://www.pythonanywhere.com/api/v0/user/hackersaggyhacker/files/path/home/hackersaggyhacker/project.zip" \
                        -H "Authorization: Token $PA_TOKEN" \
                        --form "content=@project.zip"

                    echo "Extracting ZIP into ~/djago_project ..."
                    curl -X POST "https://www.pythonanywhere.com/api/v0/user/hackersaggyhacker/consoles/execute/" \
                        -H "Authorization: Token $PA_TOKEN" \
                        --data "command=unzip -o ~/project.zip -d ~/djago_project"

                    echo "Reloading PA web app..."
                    curl -X POST "https://www.pythonanywhere.com/api/v0/user/hackersaggyhacker/webapps/hackersaggyhacker.pythonanywhere.com/reload/" \
                        -H "Authorization: Token $PA_TOKEN"
                    '''
                }
            }
        }
    }
}
