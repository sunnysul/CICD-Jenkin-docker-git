# Jenkins Docker Installation Guide
To install Jenkins using Docker, follow the steps below:
1. Pull the Jenkins Docker image from the Docker Hub:
   ```
   docker pull jenkins/jenkins:lts
   ```
2. Run the Jenkins container:
```
<!-- docker run --name myjenkins -p 8080:8080 -p 50000:50000 -v /var/jenkins_home jenkins -->
docker run --name myjenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

<!-- run on detached mode -->
docker run -d --name myjenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

<!-- check docker logs -->
```docker logs myjenkins
```