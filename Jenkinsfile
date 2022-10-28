pipeline {


  agent any

  stages {

    stage('version') {
      
      withEnv(['PYTHONPATH=C:\\Users\\apujol\\AppData\\Local\\Programs\\Python\\Python310\\python.exe']) {
      sh  'python prueba_test.py'
}

      }

    }

    stage('pip') {

      steps {

        bat 'pip list'

      }

    }

  }

}
