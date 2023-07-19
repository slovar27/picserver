pipeline {
    agent {
        label "docker1207"
    }

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        
        stage('docker ps') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
