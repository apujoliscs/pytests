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
    stage ('COMSec Login Tests ->') {
      steps {
        sh 'pytest appium_python/Resto/COMSec_LOGIN.py'
  }
}
  }
}
