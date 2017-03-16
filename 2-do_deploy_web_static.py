#!/usr/bin/python3
"""
module contains the deploy
"""
import os
from fabric.api import put, run, env


def do_deploy(archive_path):
    """
    distrubes the archives to webservers
    """
    if not os.path.exists(archive_path):
        return (False)

    env.hosts = ['54.209.54.84', '54.243.1.173']
    try:
        archive_name = archive_path.split('/')[-1].split('.')[0]
        put(archive_path, '/tmp/')
        run('sudo mkdir -p mkdir -p /data/web_static/releases/' + archive_name)
        run('sudo tar -xzf /tmp/' + archive_name +
            '.tgz -C /data/web_static/releases/' + archive_name)
        run('sudo rm /tmp/' + archive_name + '.tgz')
        run('mv /data/web_static/releases/' + archive_name +
            '/web_static/* /data/web_static/releases/' + archive_name + '/')
        run('rm -rf /data/web_static/releases/' + archive_name + '/web_static')
        run('rm -rf /data/web_static/current')
        run(' ln -s /data/web_static/releases/' + archive_name +
            '/ /data/web_static/current')
        print('New version deployed!')
        return(True)
    except:
        return(False)
