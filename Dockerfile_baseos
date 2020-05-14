FROM centos 

RUN yum install -y wget

RUN wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

RUN rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key

RUN yum install -y jenkins 

RUN yum install -y java-11-openjdk.x86_64 

RUN yum install -y net-tools

RUN yum install -y git

RUN yum install -y python3

RUN yum install -y initscripts

RUN yum install -y sudo

RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN echo "/etc/rc.d/init.d/jenkins start" >> /etc/bashrc

COPY sendmail.py /
