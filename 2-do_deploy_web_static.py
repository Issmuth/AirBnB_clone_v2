#!/usr/bin/python3
"""Distributes the archives to the webservers."""
from fabric.api import local, run, env, sudo, put
import os
env.hosts = ['100.25.2.66', '54.159.26.115']
env.user = 'ubuntu'
env.key_filename = '~/0-RSA_private_key'


def do_deploy(archive_path):
    """Deploy!!!"""
    if os.path.isfile(archive_path) is False:
        return False

    if put(archive_path, '/tmp/').failed is True:
        return False

    filename = os.path.basename(archive_path)
    file = os.path.splitext(filename)[0]

    if run('mkdir -p /data/web_static/releases/{}'
           .format(file)).failed is True:
        return False

    if run('tar -xvf /tmp/{} -C /data/web_static/releases/{}'
            .format(filename, file)).failed is True:
        return False

    if run('rm /tmp/{}'.format(filename)).failed is True:
        return False

    if run('ln -sf /data/web_static/releases/{} /data/web_static/current'
            .format(file)).failed is True:
        return False

    return True
