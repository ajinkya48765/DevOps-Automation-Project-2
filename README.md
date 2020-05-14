# Automation using Git + Docker + Jenkins + Python

#### This article is based on my project of integrating git, docker, jenkins and python under DevOps to fulfill the great industrial use case of automation. This kind of automation can help many companies for their projects.


## Problem Statement :

* *Create a container image that has jenkins installed using Dockerfile. When we launch this image it should automatically start the jenkins service in the container.
* *Create a chain of jobs which will help to fetch source code, start service, test service, notify the status and in case of failure it will have capability to launch new environment in less that a minute or may be in just 1 second.

## Solution Overview :

1. To solve this problem we are going to build chain of jobs in the jenkins each job will have their particular task :

2. But before heading towards the task we have to build our workspace so using Dockerfile we will build our workspace in our Windows, Linux or Mac. It is may be inside VM.

* Job1 : This job will continuously monitor github and as soon as found any commit it will fetch all the content in that repository and will store in the workSpace.

* Job2 : This job will identify whether the uploaded files are of HTML or PHP and accordingly it will react to launch server of corresponding language. Ex. If code is of PHP, then jenkins should start the container that has PHP already installed.

* Job3 : We will use this job for testing our application. This job will fail itself on failure of website. Which will help to trigger next job.

* Job4 : If third job failed due to any reason it means that our website is also crashed so in this scenario we should notify our developer. So we will use python script in this job to sent email to the developer.

* Job5 : It is not the part of chained jobs, This will a monitoring job which will see whether our workspace is doing well or not if found it failing it will immediately launch a new container with the same configuration.

## So lets get started . . .

* So first of all we have to create build our workspace so I have used Dockerfile to launch complete workspace in just a second or less.

* In this dockerfile I have installed softwares that I am going to use in this complete project.

[Click here to see dockerfile](https://github.com/ajinkya48765/DevOps-Automation-Project-2/blob/master/Dockerfile_baseos)

 `RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers`

* This command is used, so that our jenkins server will get sudo powers in order to modify content.

`RUN echo "/etc/rc.d/init.d/jenkins start" >> /etc/bashrc`

* This command is used to run start jenkins server inside docker. I have just appended this command inside file /etc/bashrc so that on every boot jenkins server will automatically start. This is also part of an automation. After creating this file we have build it so that we can convert it into a image.

`docker build -t <name_of_container>:<version> <path of dockerfile>`

* I used this command to build an image.

* In this picture you will find the created image. I have created with the name myjenkins and version v2.

* After creating such a great image now its time to launch it, we have to use various options while launching an image.

`docker run --it
           --privileged
           -p 7081:8080
           -v /:/base_os
           --name workSpace 
            myjenkins:v2`

* Here patting will expose 8080 port through port number 7081, I have used root as a volume because in future we have to perform some tasks through our base os.

* So in just 1 second or may less than that our new workspace will generate now we will use ip of this container to connect to jenkins.

* Actually I am using RHEL 8 as a VM so it sometimes doesn't work properly so I have launched this server on my Windows machine using tunneling. For tunneling I used ngrok.

* To setup an ngrok sever we just have to provide one command after installation

`/.ngrok http ***.***.**.***:****`

* In place of stars provide your ip address and at last provide the port gerally it is 8080 for jenkins.

* Now we are all set with our workSpace.

* Lets move towards Jobs now :

## Job1 :

* As I mentioned earlier we have to use this job for fetching data from github. So whenever developer commits this job should trigger so I have used poll SCM which will monitor the github after every one minute.

* First part of this execute shell is for futher task I will explain in it later in this article. But in the last three lines I have copied all the content from github and pasted it here my workSpace.

## Job2 : 

[Click here for HTML Dockerfile](https://github.com/ajinkya48765/DevOps-Automation-Project-2/blob/master/Dockerfile_htmlimg)

[Click here for PHP Dockerfile](https://github.com/ajinkya48765/DevOps-Automation-Project-2/blob/master/Dockerfile_phpimg)

* This job is the most important part of this project as it is going to launch the server this job is so intelligent that it automatically finds whether the webapp is written in HTML or PHP if developer provide HTML code it will launch HTML server and if provided PHP it will launch PHP server.

* For this task rather than using precreated images from dockerhub I have built my own image using docker file.

* These are the scripts for both the Dockerfiles. After creating these dockerfiles we have to configure our job.

* In this script jenkins will search for html and php extensions in that folder to identify the language of code and then accordingly use docker images. I have an example here

* Here my html_product os which I have built for production department is launched.

* So in the first job I have used first block in order to stop the container before deploying code inorder to avoid any kind of conflicts. I faced issue that if my container is on and if I pushed new content my site failes so I just remove the connection so client will not feel much glitch but in that 2 to 5 seconds an updated version will is provided.

## Job3 :

* This job will run our code on the machine and see whether it is working properly of\or not if not it will automatically fails itself so that it can trigger the notication job.

* Here I have used status environmental variable for testing.

## Job4 :

* This is basically a notifier which will share the status of container to the developer it is triggered on failure of job3. Failure of job3 concludes that our website is not properly deployed. For notifications I have used email service here. Python provides facility to send mails using script so I have used it here,

* I have also provided github link you can use it for reference.

* So finally my chain of jobs is ready and I have automated everything and also included notification feature using python.

* We can visualize it using build pipeline.


#### We have done such a huge infrastructure many advanced things but point is, what if due to any reason our workSpace fails or collaps. We will loose everything in a moment, so inorder to relaunch the infrastructure on failure, I have made one job here so It will also automated.


* Using this script I will relaunch whole infrastructure again and this completed my project. So the final list view looks like this

* This is all about this project here I have tried to automate everything and this fullfills one great industrial use case.
