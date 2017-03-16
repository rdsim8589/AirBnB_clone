#!/usr/bin/python3
"""
that creates and distributes an archive to your web
servers, using the function deploy
"""
import os
from fabric.api import local, env, task, sudo, put
from time import sleep
env.hosts = ['54.209.54.84', '54.243.1.173']


@task
def do_deploy(archive_path):
    """
    distrubes the archives to webservers
    """
    if os.path.exists(archive_path) is False:
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
        local('tar -zcf versions/web_static_' + tar_time + '.tgz \
        ./web_static')
        return ('./versions/web_static_' + tar_time + '.tgz')
    except:
        return(None)


@task
def deploy():
    """
    executes do_pack in 1-pack_web_static.py
    then
    executes do_deploy in 2-do_deploy_web_static.py
    """
    try:
        tar_path = (do_pack())
        if tar_path:
            val = do_deploy(tar_path)
            return val
    except:
        return False
