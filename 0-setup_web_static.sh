#!/usr/bin/env bash
# sets up the web server for deployment of web static

#install nginx if it doesn't exist
apt-get -y update
apt-get -y install nginx

# create required directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

#create dummy page
echo 'Web Static Deployment' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

line='server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\tadd_header X-Served-By $HOSTNAME;\n\troot   /var/www/html;\n\tindex  index.html index.htm;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html index.htm;\n\t}\n\n\tlocation /redirect_me {\n\t\treturn 301 http://cuberule.com/;\n\t}\n\n\terror_page 404 /404.html;\n\tlocation /404 {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}\n}'

echo -e $line > /etc/nginx/sites-available/default

service nginx restart
