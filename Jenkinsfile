pipeline {
  agent any
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
        sh 'allure serve pytests\reports'
  }
}
   }
}
