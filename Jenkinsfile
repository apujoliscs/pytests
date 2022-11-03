pipeline {
  agent any
   environment {
                JAVA_HOME = "C:\\Program Files\\Java\\jdk11"
            }
  stages {
    stage('Check Python Version') {
      steps {
        sh 'export -p'
        sh 'python --version'
      }
    }
    stage('Check PyTest Version') {
     steps {
        sh 'pytest --version'
      }
    }
    stage ('Send Reports to Allure') {
      steps {
        allure includeProperties: false, jdk: '11.0.11', report: 'reports', results: [[path: 'reports']]
  }
}
   }
}
