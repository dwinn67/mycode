#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
   Alta3 Research | rzfeeser@alta3.com"""

#import utilities
import shutil # shell utilities will be used to move files
import os # provies access to low level os operations (agnostic to flavor of OS)

def main():
    """called at runtime"""
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')

    # user input for new filename
    xname = input('What is the new name for kerrigan.obj? ')

    #rename existing file with new name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()


