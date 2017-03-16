#!/usr/bin/python3
"""
that creates and distributes an archive to your web
servers, using the function deploy
"""
import os
from fabric.api import local, env, task, run, put, runs_once, sudo
env.hosts = ['54.209.54.84', '54.243.1.173']


@task
def do_clean(number=0):
    '''
    cleans up the files in versions
    '''
    try:
        num = int(number)
        clean_server(num)
        clean_local(num)
    except Exception as e:
        print(e)


@task
def clean_server(num):
    '''
    cleans up the files in web_static* in the server
    '''
    directory = '/data/web_static/releases'
    try:
        if num == 0:
            num = 1
        sudo('size=$(ls -t {} | wc -l);\
        for i in $(ls -t {} | tail -n $(( $size - {} )));\
        do rm -fr $i;\
        done'.format(directory, directory, number))
    except Exception as e:
        print(e)


@runs_once
def clean_local(num):
    '''
    cleans up the files in versions locally
    '''
    try:
        local('find {} -type f ! -name "*tgz" -delete'.format(directory))
        files = local("ls -t {}".format(directory), capture=True)
        files = files.split('\n')
        if num == 0:
            num = 1
        files_to_del = ' '.join(files[num:])
        local('cd {}; rm -f {}'.format(directory, files_to_del))
    except Exception as e:
            print(e)
