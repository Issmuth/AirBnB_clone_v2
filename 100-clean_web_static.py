#!/usr/bin/python3
"""Cleaner."""
from fabric.api import local, run
import os


def do_clean(number=0):
    """clean old archive."""
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archs = sorted(os.listdir('versions'))

    archs.pop() for i in range(number)
    local("rm versions/{}".format(a)) for a in archs

    with cd("/data/web_static/releases"):
    archs = run("ls -tr").split()
    archs = a for a in archives if "web_static_" in a
    archs.pop() for i in range(number)
    [run("rm -rf ./{}".format(a)) for a in archs]
