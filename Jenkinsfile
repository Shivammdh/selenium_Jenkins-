pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Shivammdh/Selenium_Python_Project.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Shivammdh/Selenium_Python_Project.git'
                
            }
        }
        stage('Test') {
            steps {
                sh 'python3 test.py'
            }
        }
    }
}
