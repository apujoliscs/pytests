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
    stage ('Run Dialer, tipe some numbers & make a call') {
      steps {
        sh 'python appium_python/Resto/Abrir_Calculadora.py'
  }
}
  }
}
