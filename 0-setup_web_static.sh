#!/usr/bin/env bash
# install and configure arbnb static

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data
sudo chown -R ubuntu:ubuntu /data

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

HTML="Holberton school - test"

sudo echo -e "$HTML" | sudo tee /data/web_static/releases/test/index.html

rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

line="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "43i\ $line" /etc/nginx/sites-available/default

sudo service nginx restart
