#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# If you want the downloaded cli zip deleted
rm -rf aws && rm awscliv2.zip

sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv

PROJECT_NAME="$1"
PROJECT_DIR="/vagrant/$PROJECT_NAME"

cd "$PROJECT_DIR"
python3 -m venv venv-vm
source venv-vm/bin/activate
python -m pip install -r requirements.txt

echo "cd $PROJECT_DIR" >> /home/vagrant/.bashrc
echo "source venv-vm/bin/activate" >> /home/vagrant/.bashrc
