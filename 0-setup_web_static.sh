#!/usr/bin/env bash
# setup web server for deplyment of web_static
dpkg -s nginx
if [ "$echo $?" -ne 0 ]; then
    apt-get update
    sudo apt-get -y install nginx
fi
DIR="/data/web_static/releases/test /data/web_static/shared/"
for dir in $DIR; do
    if [ ! -d $dir ]; then
	sudo mkdir -p $dir
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
if [ -d $SYMBOLIC ]; then
    sudo rm -rf $SYMBOLIC
fi
sudo ln -s /data/web_static/releases/test $SYMBOLIC

DIR="/data/"
sudo chown -R ubuntu:ubuntu $DIR
