#!/usr/bin/env python3

# This script determines the machine’s local IPV4 address, 
# locates all files with the extension “cfg” in /mnt/configFiles/, 
# and recursively replaces all occurrences of “zillow.com” within that file with that IP, 
# and then changes the extension of each of those files to .conf.  
# David Hart 04.07.2018

import socket
import os
import shutil

def move(src, dest):
    shutil.move(src, dest)

def local_ip():
    return socket.gethostbyname(socket.getfqdn())

def main():
    new_ip = (local_ip())
    for file in os.listdir("/mnt/configFiles"):
        if file.endswith(".cfg"):
            target_filepath = (os.path.join("/mnt/configFiles", file))
            with open(target_filepath, 'r') as file :
                filedata = file.read()
                filedata = filedata.replace('zillow.com', new_ip)
            with open(target_filepath, 'w') as file:
                file.write(filedata)
                file.close()
            file_mod = target_filepath.replace(".cfg",".conf")
            move(target_filepath, file_mod)

main()
