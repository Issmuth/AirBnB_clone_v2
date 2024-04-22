#!/usr/bin/python3
import sys
sys.path.append('..')
from models import storage

all = storage.all('State')
for item in all.values():
    print (item.id)
