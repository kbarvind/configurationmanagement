'''
Created on Mar 5, 2020

@author: kbarvind
'''

import platform
import os
from builtins import staticmethod

class OSInfo(object):
    
    @staticmethod
    def getPlatformSystem():
        return platform.system().lower()
    
    @staticmethod
    def getPlatformLinuxDistribution():
        return platform.linux_distribution()
    
    @staticmethod
    def getPlatformRelease():
        return platform.release().lower()
    
    @staticmethod
    def getOS():
        return os.name.lower()
    
    @staticmethod
    def getPATHEnvironemnt():
        return os.getenv("PATH", None)
    
    
    @staticmethod
    def getPathSeperator():
        return os.path.sep
    
    @staticmethod
    def getUserHome():
        return os.environ['HOME']
    
    
    @staticmethod
    def getPathVariableSeprator():
        if OSInfo.getPlatformSystem() == "windows":
            return ";"
        else:
            return ":"
        
    @staticmethod
    def getEnvironment(var_name):
        return os.getenv(var_name, None)
    




