#!/usr/bin/python3
"""
that creates and distributes an archive to your web
servers, using the function deploy
"""
import os
from fabric.api import local, env, task, run, put, runs_once
env.hosts = ['54.209.54.84', '54.243.1.173']


@runs_once
def do_pack():
    """
    creates a version_folder
    compresses all files found in web_static
    """
    if not os.path.exists('versions'):
        os.mkdir('versions')
    try:
        tar_time = local('date +%Y%m%d%H%M%S', capture=True)
        local('tar -zcf versions/web_static_{}.tgz ./web_static'.
              format(tar_time))
        return ('./versions/web_static_' + tar_time + '.tgz')
    except:
        return(None)


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
        run('mkdir -p {}'.format(tar_path))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(archive_name, tar_path))
        run('rm /tmp/{}.tgz'.format(archive_name))
        run('mv {}/web_static/* {}/'.format(tar_path, tar_path))
        run('rm -rf {}/web_static'.format(tar_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(tar_path))
        print('New version deployed!')
        return(True)
    except:
        return(False)


@task
def do_clean(number=0):
    '''
    cleans up the files in versions
    '''
    try:
        clean_server(number)
        clean_local(number)
    except Exception as e:
        print(e)


@task
def clean_server(number):
    '''
    cleans up the files in web_static* in the server
    '''
    directory = '/data/web_static/releases'
    try:
        num = int(number)
        directories = run('size=$(ls -t {} | wc -l;\
        for i in $(ls -t {} | tail -n $(( $size - {} )));\
        do rm -fr $i;\
        done'.format(directory, number, number))
    except Exception as e:
        print(e)


@runs_once
def clean_local(number):
    '''
    cleans up the files in versions locally
    '''
    try:
        num = int(number)
        local('find {} -type f ! -name "*tgz" -delete'.format(directory))
        files = local("ls -t {}".format(directory), capture=True)
        files = files.split('\n')
        if num == 0:
            num = 1
        files_to_del = ' '.join(files[num:])
        local('cd {}; rm -f {}'.format(directory, files_to_del))
    except Exception as e:
            print(e)


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
