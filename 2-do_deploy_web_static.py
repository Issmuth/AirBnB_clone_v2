#!/usr/bin/python3
"""Distributes the archives to the webservers."""
from fabric.api import local, run, env, sudo, put
import os
env.hosts = ['100.25.2.66', '54.159.26.115']
env.user = 'ubuntu'
env.key_filename = '~/0-RSA_private_key'


def do_deploy(archive_path):
    """Deploy!!!"""
    put(archive_path, '/tmp/')
    filename = os.path.basename(archive_path)
    file = os.path.splitext(filename)[0]

    run('mkdir -p /data/web_static/releases/{}'.format(file))
    run('tar -xvf /tmp/{} -C /data/web_static/releases/{}'
        .format(filename, file))
    run('rm /tmp/{}'.format(filename))

    run('ln -sf /data/web_static/releases/{} /data/web_static/current'
        .format(file))
