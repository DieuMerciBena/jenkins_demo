pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DieuMerciBena/jenkins_demo/edit/main/Jenkinsfile.git'
            }
        }
        stage('Deploy via Ansible') {
            steps {
                sh 'ansible-playbook -i hosts deploy_flask.yaml'
            }
        }
    }
    post {
        success {
            echo 'Déploiement réussi !'
        }
        failure {
            echo 'Échec du déploiement !'
        }
    }
}
