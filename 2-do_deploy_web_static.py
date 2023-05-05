#!/usr/bin/python3
"""A module that compresses the web static folder
   and deploys it to two web servers"""
from fabric.api import local
import datetime
import os


env = {
    'key_filename': '~/.ssh/id_rsa',
    'user': 'ubuntu',
    'host': ['54.84.251.92', '54.90.50.38']
}


def do_pack():
    """generates a .tgz archive

    Return: path to archive on success; None on fail
    """

    now = datetime.datetime.now()
    filename = 'web_static_{}.tgz'.format(now.strftime('%Y%m%d%H%M%S'))
    local("mkdir -p versions")
    info = local("tar -cvzf versions/{} web_static".format(filename))
    if info.succeeded:
        return 'versions/{}'.format(filename)
    return None


def do_deploy(archive_path):
    """Distributes an archive to two web servers

    Return: True if all operations have been done correctly,
            otherwise returns False
    """
    if not os.path.isfile(archive_path):
        return False

    result1 = put(archive_path, '/tmp/')
    filename = archive_path.split('/')[-1]
    compressed = '/tmp/' + filename
    uncompressed = "/data/web_static/releases/" + filename.split('.')[0]

    result2 = run("sudo mkdir -p {}".format(uncompressed))
    result3 = run("sudo tar -xzf {} -C {}".format(compressed, uncompressed))
    result4 = run("sudo rm {}".format(compressed))
    link_path = '/data/web_static/current'
    result5 = run("sudo ln -sf {} {}".format(uncompressed, link_path))

    if all([result1.succeeded, result2.succeeded, result3.succeeded,
           result4.succeeded, result5.succeeded]):
        return True
    return False
