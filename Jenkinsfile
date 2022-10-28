pipeline {
  agent any
  stages {
    stage('Setup Python Virtual ENV') {
        steps {
          script {
            sh '''
            chmod +x envsetup.sh
            ./envsetup.sh
            '''}
        }
        }
    }
}
