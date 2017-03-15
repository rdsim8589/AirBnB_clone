#!/usr/bin/python3
"""
this module contains the method do_pack
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
        local('sudo tar -zcf ./versions/web_static_$(date +%Y%m%d%H%M%S).tgz\
        ./web_static')
        return (os.path.abspath('./versions'))
    except:
        return(None)
