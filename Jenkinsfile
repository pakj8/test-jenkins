pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo/fastapi-scraper.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-scraper .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 fastapi-scraper'
            }
        }
    }
}
