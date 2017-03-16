#!/usr/bin/python3
"""
module contains the deploy
"""
import os
from fabric.api import put, sudo, env, task


env.hosts = ['54.209.54.84', '54.243.1.173']


@task
def do_deploy(archive_path):
    """
    distrubes the archives to webservers
    """
    if not os.path.exists(archive_path):
        return (False)
    try:
        archive_name = archive_path.split('/')[-1].split('.')[0]

        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/' + archive_name)
        sudo('tar -xzf /tmp/' + archive_name +
             '.tgz -C /data/web_static/releases/' + archive_name)
        sudo('rm /tmp/' + archive_name + '.tgz')
        sudo('mv /data/web_static/releases/' + archive_name +
             '/web_static/* /data/web_static/releases/' + archive_name + '/')
        sudo('rm -rf /data/web_static/releases/\
        ' + archive_name + '/web_static')
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s /data/web_static/releases/' + archive_name +
             '/ /data/web_static/current')
        print('New version deployed!')
        return(True)
    except:
        return(False)
