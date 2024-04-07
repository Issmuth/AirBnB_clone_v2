#!/usr/bin/python3
"""Full deployment, archiving and moving."""
from fabric.api import local, run, env, sudo, put
from datetime import datetime
import os

env.hosts = ["100.25.2.66", "54.159.26.115"]
env.user = 'ubuntu'
env.key_filename = '~/0-RSA_private_key'


def do_pack():
    """Packing function."""

    local("mkdir -p versions")
    name = "versions/web_static_" + datetime.now().strftime("%Y%m%d%H%M%S")
    result = local("tar -czvf {}.tgz web_static".format(name))
    if result.failed is True:
        return None
    else:
        return ("{}.tgz".format(name))


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

    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(filename, file)).failed is True:
        return False

    if run('mv /data/web_static/releases/{}/web_static/* '
           '/data/web_static/releases/{}/'.format(file, file)).failed is True:
        return False

    if run('rm -rf /data/web_static/releases/{}/web_static'.format(file)).failed is True:
        return False

    if run('rm /tmp/{}'.format(filename)).failed is True:
        return False

    if run('rm -rf /data/web_static/current').failed is True:
        return False

    if run('ln -sf /data/web_static/releases/{} /data/web_static/current'
            .format(file)).failed is True:
        return False

    if sudo('service nginx restart').failed is True:
        return False
    print("New version deployed!")
    return True


def deploy():
    """Combination of pack and deploy."""
    path = do_pack()
    print(path)
    if path is None:
        return False

    ret = do_deploy(path)
    return (ret)
