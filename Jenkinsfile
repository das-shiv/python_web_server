pipeline {
    agent any
    
    stages {
        stage('Run Unit Test') {
            steps {
                sh 'python3 -m unittest test_atg_world_connection'
            }
        }
    }
}
