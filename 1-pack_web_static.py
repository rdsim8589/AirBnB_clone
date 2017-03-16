#!/usr/bin/python3
"""
this module contains the method do_pack
fab -f 1-pack_web_static.py do_deploy:archive_path=<tar file> /
    -i <ssh key> -u ubuntu
"""
from fabric.api import local, task
import os


@task
def do_pack():
    """
    creates a version_folder
    compresses all files found in web_static
    """
    if not os.path.exists('versions'):
        os.mkdir('versions')
    try:
        tar_time = local('date +%Y%m%d%H%M%S', capture=True)
        local('sudo tar -zcf ./versions/web_static_' + tar_time + '.tgz \
        ./web_static')
        return (os.path.abspath('./versions/web_static_' + tar_time + '.tgz'))
    except:
        return(None)
