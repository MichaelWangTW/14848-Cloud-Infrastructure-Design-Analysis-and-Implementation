### Pull the docker image from DuckerHub and create terminal program. Push to my own DockerHub
1. Hadoop NameNode
2. Hadoop DataNode
3. Apache Spark
4. Jupyter NoteBook
5. SonarQube and SonarScanner
6. Terminal

### Following steps were done on GCP cloud shell
1. Create new project on GCP, note down the project ID (mini-project-submit)

2. Pull all 5 docker images, tag them and push them to Google Container Registry, respectively 
``` sh
docker pull michaelwangtw/terminal
docker tag michaelwangtw/terminal gcr.io/{your-project-id}/michaelwangtw/terminal:latest
docker push gcr.io/{your-project-id}/michaelwangtw/terminal:latest

docker pull michaelwangtw/hadoop
docker tag michaelwangtw/hadoop gcr.io/{your-project-id}/michaelwangtw/hadoop:latest
docker push gcr.io/{your-project-id}/michaelwangtw/hadoop:latest

docker pull michaelwangtw/jupyter-notebook
docker tag michaelwangtw/jupyter-notebook gcr.io/{your-project-id}/michaelwangtw/jupyter-notebook:latest
docker push gcr.io/{your-project-id}/michaelwangtw/jupyter-notebook:latest

docker pull michaelwangtw/spark
docker tag michaelwangtw/spark gcr.io/{your-project-id}/michaelwangtw/spark:latest
docker push gcr.io/{your-project-id}/michaelwangtw/spark:latest

docker pull michaelwangtw/sonarqube
docker tag michaelwangtw/sonarqube gcr.io/{your-project-id}/michaelwangtw/sonarqube:latest
docker push gcr.io/{your-project-id}/michaelwangtw/sonarqube:latest
```

3. Create new Kubernetes cluster on GCP via GUI

4. Go to Container Registry in GCP and deploy five docker image I mentioned above. This action can be done via GUI.

5. Go back to GKE cluster and check if pods are running


