#!/usr/bin/python

import sys, os

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'System Spec:', str(sys.argv)

with open('data.txt', 'w') as f:
    data = str(sys.argv[1:])[4:-3].replace("', 'u","\n")
    f.write(data)
    f.close()


