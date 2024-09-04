# Hello World Microservices Application

This project is a Microservices application consisting of Flask, Express, and Spring Boot components. Each service is containerized using Docker and is deployed on Google Kubernetes Engine (GKE).
The goal of this application is to get familiar with the basic concepts of microservices architecture.\
These application is currently up and running on GKE cluster. 

#


### The application is divided in 3 major services

#### 1. Hello Service: 

This micro-service is written using Java and SpringBoot Frmaework.\
The service is hosted on following endpoint: [http://34.94.35.116/hello](http://34.94.35.116/hello).

This returns a Json response with message as "Hello".

    {
      message : "Hello"
    }
###### Based on the usage, cluster pods may have been scaled down to save resources.    

#

#### 2. World Service:

This micro-service is written using Javascript and ExpressJS Frmaework. \
The service is hosted on following endpoint: [http://34.94.193.46/world](http://34.94.193.46/world).

This returns a Json response with message as "World".

    {
      message : "World"
    }
###### Based on the usage, cluster pods may have been scaled down to save resources.

#

#### 3. Hello-World web-application
This webapplication is written using Python and Flask Frmaework.\
This app makes call to other two service endpoint and display message : "Hello World". \
The web-app is hosted on : [http://34.94.205.204‎](http://34.94.205.204‎)

###### Based on the usage, cluster pods may have been scaled down to save resources.



#
## Resources

Here are the resources and links for accesing the Docker Images.\ 
### This Docker Hub repo has all the latest docker images hosted on GKE
  - #### [Docker Hub Repo Link (click here)](https://hub.docker.com/u/shan25) 
  - [hello-world-springboot](https://hub.docker.com/r/shan25/hello-world-springboot)
  - [hello-world-expressjs](https://hub.docker.com/r/shan25/hello-world-expressjs)
  - [hello-world-flask](https://hub.docker.com/r/shan25/hello-world-flask)


## Getting Started


### Prerequisites 
- Docker
- Node.js
- Python3
- Java 17
- VScode IDE

### Running the components on local

##### For ExpressJs 

    cd express
    npm install
    node server.js

To build and run docker image :
    
    docker build -t express-app .
    docker run -p 3000:3000 express-app


##### For Springboot 

    cd springBoot/hello
    mvn clean install
    java -jar target/hello-0.0.1-SNAPSHOT.jar

To build and run docker image :
    
    docker build -t springboot-app .
    docker run -p 8080:8080 springboot-app

##### For Flask 

    cd flask_helloWorld
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py

To build and run docker image :
    
    docker build -t flask-app .
    docker run -p 5000:5000 flask-app


End with an example of getting some data out of the system or using it
for a little demo

## Accessing the Applications 
### On local host
- Express: Access at http://localhost:3000 \
- Flask: Access at http://localhost:5000 \
- Spring Boot: Access at http://localhost:8080 \

### On cloud 
- Spring Boot: Access at [http://34.94.35.116/hello](http://34.94.35.116/hello) \
- Express: Access at [http://34.94.193.46/world](http://34.94.193.46/world) \
- Flask: Access at [http://34.94.205.204‎](http://34.94.205.204‎)

## Scaling up/down on GKE

Images are deployed on GKE.\
To scale up the applications, login to gcloud through cli and run following command:

    kubectl scale deployment flask-app --replicas=2
    kubectl scale deployment express-app --replicas=2
    kubectl scale deployment springboot-app --replicas=2

To scale down, 

    kubectl scale deployment flask-app --replicas=0
    kubectl scale deployment express-app --replicas=0
    kubectl scale deployment springboot-app --replicas=0


## Authors

  - **Shantanu Joshi** - *[LinkedIn](https://www.linkedin.com/in/shantanujoshi25/)* -

