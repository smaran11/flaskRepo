pipeline {
    agent any

    stages {
        stage('SCM checkout') {
            steps{
                git branch: 'main', url: 'https://github.com/smaran11/flaskRepo.git' 
            }
        }
        stage ('Docker image build'){
            steps{
                sh '/usr/bin/docker image build -t smaranm/flask-image .'
            }
        }
        stage ('Docker login'){
            steps{
                sh 'echo dckr_pat_ISxSPc2DrvgTXQmpCdR4ZqpwMl8 | /usr/bin/docker login -u smaranm --password-stdin'
            }
        }
        stage ('Docker image push'){
            steps{
                sh '/usr/bin/docker image push smaranm/flask-image'
            }
        }
        stage ('Remove service'){
            steps{
                sh '/usr/bin/docker service rm service1'
            }
        }
        stage ('create service'){
            steps{
                sh '/usr/bin/docker service create --name service1 -p 4000:4000 --replicas 2 smaranm/flask-image'
            }
        }
    }
}
