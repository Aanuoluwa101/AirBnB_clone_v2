#!/usr/bin/env bash
"""A module that generates a .tgz file using fabric"""
from fabric.api import local
import datetime

def do_pack():
    """generates a .tgz archive

    Return: path to archive on success; None on fail
    """

    now = datetime.datetime.now()
    filename = 'web_static_{}.tgz'.format(now.strftime('%Y%m%d%H%M%S'))
    info = local("mkdir -p versions && tar -cvzf versions/{} web_static".format(filename))
    
    if info.succeeded:
        return 'versions/{}'.format(filename)
    return None
