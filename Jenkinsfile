pipeline {
    agent any

    stages {

        stage('Install System Dependencies') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip python3-venv wget unzip gnupg
                '''
            }
        }

        stage('Install Chrome') {
            steps {
                sh '''
                wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
                echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list
                apt-get update
                apt-get install -y google-chrome-stable
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --alluredir=allure-results
                '''
            }
        }

        stage('Install Allure') {
            steps {
                sh '''
                wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.27.0/allure-commandline-2.27.0.tgz
                tar -xzf allure-commandline-2.27.0.tgz
                '''
            }
        }

        stage('Generate Report') {
            steps {
                sh '''
                ./allure-2.27.0/bin/allure generate allure-results --clean -o allure-report
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
        }
    }
}