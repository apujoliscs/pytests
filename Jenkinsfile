pipeline {
  agent any
  stages {
    stage('Check Python Version') {
      steps {
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
        JAVA_HOME='/Program Files/Java/jdk11'
        sh 'allure serve /appium_python'
  }
}
   }
}
