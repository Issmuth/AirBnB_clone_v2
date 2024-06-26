#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

#create dummy page
echo 'Web Static Deployment' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

line="server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\tadd_header X-Served-By $HOSTNAME;\n\troot   /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\n\tserver_name _;\n\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html index.htm;\n\t}\n\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=xvFZjo5PgG0&pp=ygUJcmljayByb2xs;\n\t}\n\n\terror_page 404 /404.html;\n\tlocation /404 {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}\n}"

echo -e "$line" > /etc/nginx/sites-available/default

service nginx restart
