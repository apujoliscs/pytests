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
        sh 'pip install allure'
        sh 'pytest --version'
      }
    }
    stage ('COMSec Login Tests ->') {
      steps {
        sh 'pytest COMSec_LOGIN_test.py'
  }
}
  }
}
