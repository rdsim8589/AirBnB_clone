#!/usr/bin/env bash
# setup web server for deplyment of web_static
dpkg -s nginx
if [ "$echo $?" -ne 0 ]; then
    apt-get update
    sudo apt-get -y install nginx
fi
DIR="/data/web_static/releases/test /data/web_static/shared/"
for dir in $DIR; do
    if [ ! -d "$dir" ]; then
	sudo mkdir -p "$dir"
    fi
done
FILE="/data/web_static/releases/test/index.html"
if [ ! -f $FILE ]; then
    echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee $FILE
fi
SYMBOLIC="/data/web_static/current"
sudo ln -fs /data/web_static/releases/test $SYMBOLIC

DIR="/data/"
sudo chown -R ubuntu:ubuntu $DIR
sed -i '37i \\tlocation /hbnb_static/ \{\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm;\n\t\tautoindex on;\n\t\}' /etc/nginx/sites-available/default
