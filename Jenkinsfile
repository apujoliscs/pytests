pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('hello') {
      steps {
        sh 'pytest --version'
      }
    }
    stage ('Ahorita') {
      steps {
        sh 'python /appium_python/Resto/COMSec_LOGIN_test.py'
  }
}
