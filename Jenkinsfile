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
        sh 'pip install allure-pytest'
        sh 'pip install allure-python-commons'
        sh 'pip install Appium-Python-Client'
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
