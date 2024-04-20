#!/usr/bin/bash
from fabric.api import local

def test():
    results = local('ls -ltr')
    for result in results:
        print(result)
