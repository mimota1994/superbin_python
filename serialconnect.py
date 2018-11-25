# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:41:14 2018

@author: mimota
"""
import serial

class Ser(object):
    def __init__(self, port, baudrate = 9600, 
                 bytesize = 8, parity = 'E', 
                 stopbits = 1, timeout = None):
        
        self.port = serial.Serial(port, baudrate,
                                  bytesize, parity,
                                  stopbits, timeout)
    
    def send_cmd(self, cmd):
        self.port.write(cmd)
        print('send command : %s success'%cmd.decode("utf-8"))
        #response = self.port.readall()
        #response = self.convert_hex(response)
        #return response
    
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result
    
    def listen_port(self, length):
        #flag = True
        print("length is %d"%length)
        response = self.port.read(length)
        #while(flag):
            #response = self.port.read(2)
            #if(response == 'ok'):
                #flag = False
        return response
    
    
    
#plist = list(serial.tools.list_ports.comports())

#if(len(plist) <= 0):
    #print("no port")
#else:
    #plist