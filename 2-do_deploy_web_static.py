#!/usr/bin/python3
"""
module contains the deploy
use case
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=<tar file> /
    -i <ssh key> -u ubuntu
"""
import os
from fabric.api import put, sudo, env, task


env.hosts = ['54.209.54.84', '54.243.1.173']


@task
def do_deploy(archive_path):
    """
    distrubes the archives to webservers
    """
    if not os.path.isfile(archive_path):
        return (False)
    try:
        archive_name = archive_path.split('/')[-1].split('.')[0]
        tar_path = '/data/web_static/releases/' + archive_name
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}'.format(tar_path))
        sudo('tar -xzf /tmp/{}.tgz -C {}'.format(archive_name, tar_path))
        sudo('rm /tmp/{}.tgz'.format(archive_name))
        sudo('mv {}/web_static/* {}/'.format(tar_path, tar_path))
        sudo('rm -rf {}/web_static'.format(tar_path))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {} /data/web_static/current'.format(tar_path))
        print('New version deployed!')
        return(True)
    except:
        return(False)


"""
this module contains the method do_pack
fab -f 1-pack_web_static.py do_deploy:archive_path=<tar file> /
    -i <ssh key> -u ubuntu
"""


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
        local('run tar -zcf ./versions/web_static_' + tar_time + '.tgz \
        ./web_static')
        return (os.path.abspath('./versions/web_static_' + tar_time + '.tgz'))
    except:
        return(None)
