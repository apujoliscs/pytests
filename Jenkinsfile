pipeline {
  agent any
  stages {
    stage('Check Python Version') {
      steps {
        sh 'python --version'
      }
    }
      stage('Example') {
        steps {
        echo "Running ${env.JAVA_HOME} on ${env.C:/Program Files/Java/jdk1.8}"
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
