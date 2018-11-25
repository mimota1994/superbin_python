# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:37:32 2018

@author: mimota
"""
import os, signal, subprocess

def cameraLogin():
    print("trying to recognize")
    zbarcam = subprocess.Popen("zbarcam --raw --nodisplay /dev/video0",
                              stdout = subprocess.PIPE, shell = True, preexec_fn = os.setsid)

    try:
        #qrcodetext = None
    #while(qrcodetext):
        qrcodetext = zbarcam.stdout.readline()
    finally:
        os.killpg(zbarcam.pid, signal.SIGTERM)
        return qrcodetext
    
