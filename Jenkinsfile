pipeline {
  agent any
  tools {
    jdk 'JAVA_HOME'
  }

  stages {
    stage('jdk 8') {
      steps {
        sh 'java -version'
        sh 'javac -version'
        withEnv(["JAVA_HOME=${tool 'openjdk_1.6.0_45'}", "PATH=${tool 'openjdk_1.6.0_45'}/bin:${env.PATH}"]) {
        sh 'java -version'
        sh 'javac -version'
        }
      }
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
