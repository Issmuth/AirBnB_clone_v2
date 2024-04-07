#!/usr/bin/python3
"""Creates an archive of the web_static folder."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Packing function."""

    local("mkdir -p versions")
    name = "versions/web_static_" + datetime.now().strftime("%Y%m%d%H%M%S")
    result = local("tar -czvf {}.tgz web_static".format(name))
    if result.failed:
        return None
    else:
        return ("versions/{}.tgz".format(name))
