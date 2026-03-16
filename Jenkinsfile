pipeline {
    agent any

    stages {

        stage('Install Python') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --alluredir=allure-results'
            }
        }

        stage('Generate Report') {
            steps {
                sh '''
                apt-get install -y default-jre
                curl -o allure.tgz -L https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.tgz
                tar -xvzf allure.tgz
                ./allure-2.24.0/bin/allure generate allure-results --clean -o allure-report
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