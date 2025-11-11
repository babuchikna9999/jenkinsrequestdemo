pipeline{
    agent any

    environment{
        PYTHON="C:\Users\Lenovo\AppData\Local\Programs\Python\Python314\python.exe"
    }

    stages{
        stage("Checkout code"){
            steps{
                checkout scm
            }
        }
        stage("Installing dependencies"){
            steps{
                bat "pip install -r requirements.txt"
            }
        }
        stage("extracting data from api"){
            steps{
                bat "${env.PYTHON} extract.py"
            }
        }
    }

    post{
        success{
            echo "pipeline executed successfully..."
        }
        failed{
            echo "something wents wrong..."
        }
        always{
            echo "cleaning resources..."
        }
    }
}