#!/usr/bin/python2.7
#-*-coding=utf-8-*-

import os

def run(**args):

    print "[*] In dirlister modules."
    files = os.listdir(".")
    print str(files)

    return str(files)
