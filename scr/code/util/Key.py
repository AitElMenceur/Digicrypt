#!/usr/bin/python
# -*- coding: utf-8 -*-
class Format:
    def __init__(self, value):
        self.key = value
    def Format1(self):
        return self.key[0:4]
    def __str__(self):
        return self.key

class Key(Format) :
    def __init__(self, value):
        self.key = value

        
    