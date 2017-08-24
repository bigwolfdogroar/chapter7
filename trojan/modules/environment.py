#!/usr/bin/python2.7

import os

def run(**args):
    print "[*] In environment modules."
    return str(os.environ)
