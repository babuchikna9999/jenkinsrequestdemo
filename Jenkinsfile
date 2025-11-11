pipeline{
    agent any

    environment{
        PYTHON="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
        API_TOKEN=credentials("API_TOKEN")
    }

    stages{
        stage("Checkout code"){
            steps{
                checkout scm
            }
        }
        stage("Installing dependencies"){
            steps{
                bat '${env.PYTHON} -m pip install -r requirements.txt'
            }
        }
        stage("extracting data from api"){
            steps{
                bat '''
                SET API_TOKEN=%API_TOKEN%
                %PYTHON% extract.py
                '''
            }
        }
    }

    post{
        success{
            echo "pipeline executed successfully..."
        }
        failure{
            echo "something wents wrong..."
        }
        always{
            echo "cleaning resources..."
        }
    }
}