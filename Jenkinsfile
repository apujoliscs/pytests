pipeline {
  agent any
  tools {
    jdk 'jdk_1.8.0_151'
  }

  stages {
    stage('jdk 8') {
      steps {
        sh 'java -version'
        sh 'javac -version'
      }
    }
    stage('jdk 6') {
      steps {
        withEnv(["JAVA_HOME=${tool 'openjdk_1.6.0_45'}", "PATH=${tool 'openjdk_1.6.0_45'}/bin:${env.PATH}"]) {
          sh 'java -version'
          sh 'javac -version'
        }
      }
    }
    stage('global jdk') {
      steps {
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
