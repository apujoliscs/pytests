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
    stage ('COMSec Login Tests') {
      steps {
        sh 'pytest -v -s --alluredir="/appium_python" COMSec_LOGIN_test.py'
  }
}
    stage ('Send Reports to Allure') {
      steps {
        sh 'allure serve /appium_python'
  }
}
   }
}
