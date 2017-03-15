#!/usr/bin/env bash
# check if package is installed
dpkg -s nginx
if [ "$echo $?" -ne 0 ]; then
    apt-get update
    sudo apt-get -y install nginx
fi
# creates the directories of the two given paths
DIR="/data/web_static/releases/test /data/web_static/shared/"
for dir in $DIR; do
    if [ ! -d "$dir" ]; then
	sudo mkdir -p "$dir"
    fi
done
# push a test index file into test
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
# creates a symbolic link
SYMBOLIC="/data/web_static/current"
sudo ln -fs /data/web_static/releases/test $SYMBOLIC

# recursively change the owner and group
DIR="/data/"
sudo chown -R ubuntu:ubuntu $DIR
# configure to serve /hbnb_static check if inserting at the correct line
sudo sed -i '37i \\tlocation /hbnb_static/ \{\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm;\n\t\tautoindex on;\n\t\}' /etc/nginx/sites-available/default
sudo service nginx restart
