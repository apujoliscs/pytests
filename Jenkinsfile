pipeline {
  agent any
   environment {
                JAVA_HOME = '../../../Program Files\Java\jdk1.8'
            }
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
        sh 'allure serve /appium_python'
  }
}
   }
}
