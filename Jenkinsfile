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
    stage ('Run Calculator & tipe some numbers') {
      steps {
        sh 'python appium_python/Resto/Abrir_Calculadora.py'
  }
}
  }
}
