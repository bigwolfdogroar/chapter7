#!/usr/bin/python2.7

import os

def run(**args):
    print "[*] In environment modules."
    print str(os.environ)
    return str(os.environ)
