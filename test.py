#!/usr/bin/python3
"""Test modue for the space base"""

from models.Space_Base import SpaceBase
from models import storage

for obj in storage.all().values():
    print(obj)

base = SpaceBase()
#print(base)
base.save()
