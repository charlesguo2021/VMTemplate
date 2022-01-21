#!/usr/bin/python

import os, sys

# Open a file
path = "/etc/ansible/vars"
dirs = os.listdir( path )

# Find the config file with smallest number
print(min(dirs))
