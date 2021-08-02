import os
from collections import defaultdict
from os import path

#https://en.wikipedia.org/wiki/Autovivification
class Tree(dict):
    """Perl-autovivification is the automatic creation of new arrays and hashes as required every time an undefined value is dereferenced"""
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


class AppConfig(object):
    def __init__(self):
        dir = path.dirname(__file__)
        self.config_file = open(dir+"/router_file.txt", "r")

    def loadConfig_map(self):
        #To achive 0(1) operation, KV/Hashmap will help
        kvMap = Tree()
        for line in self.config_file:
            key=line.split("=")
            nesteddKey=key[0].split(".")
            kvMap[nesteddKey[0]][nesteddKey[1]][nesteddKey[2]][nesteddKey[3]]=key[1].replace("\n","")
        return kvMap

# Create a singleton version of the config to be used throughout the app
loadConfig=AppConfig()