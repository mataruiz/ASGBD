#!/usr/bin/python

import sys
import os

os.system('mysql --user=' + sys.argv[1] + ' --password=' + sys.argv[2] + ' --database=' + sys.argv[3])
