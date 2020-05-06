#!/usr/bin/python
# -*- coding: utf-8 -*-
class Format:
    def __init__(self, value):
        self.key = value
    
    def __str__(self):
        return self.key
    def Format1(self):
        return self.key[0:4]
    def AES(self):
        return hex(int(str(self), 16))[0:15]
    def DES(self):
        return hex(int(str(self), 16))[0:3]
    def RC(self):
        return hex(int(str(self), 16))[0:15]
    def Misty(self):
        return hex(int(str(self), 16))[0:7]
class Key(Format) :
    def __init__(self, value):
        self.key = value



        
    