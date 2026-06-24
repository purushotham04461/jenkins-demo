#!/bin/bash
# install jenkins in ec2
sudo yum update -y
sudo wget -O /etc/yum.repos.d/jenkins.repo \
https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

sudo dnf install java-21-amazon-corretto -y

sudo yum install jenkins -y

sudo systemctl enable jenkins

sudo systemctl start jenkins

sudo yum install git -y

# git push commands
python3 demo.py

touch index.py

git config --global user.name "purushotham04461"
git config --global user.email "spurushotham0446@gmail.com"

git add .

git commit -m "Added index.py" || true

git remote set-url origin https://purushotham04461:YOUR_NEW_GITHUB_TOKEN@github.com/purushotham04461/jenkins-demo.git

git push origin HEAD:main
