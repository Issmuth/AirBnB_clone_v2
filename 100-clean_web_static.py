#!/usr/bin/python3
"""Cleaner."""
from fabric.api import local, run, env, lcd, cd
import os

env.hosts = ['100.25.2.66', '3.86.7.177']
env.user = ['ubuntu']
env.key_filename = '~/0-RSA_private_key'

def do_clean(number=0):
    """clean old archive."""
    if int(number) == 1 or int(number) == 0:
        num = 1
    else:
        num = int(number)

    webs = sorted(os.listdir("versions"))
    web = []
    for i in range(num):
        a = webs.pop()

    for w in webs:
        if "web_static_" in w:
            web.append(w)

    for w in web:
        local("rm versions/{}".format(w))
"""
    web_dirs = run("ls -tr /data/web_static/releases").split()
    dirs = []
    for a in web_dirs:
        if "web_static_" in a:
            dirs.append(a)

    for i in range(num):
        dirs.pop()

    for a in dirs:
        run("rm -rf ./{}".format(a))"""
