'''
Created on 20-May-2021

@author: kbarvind
'''

import logging
from app.boxconfig.plugin.pluginfactory import BoxConfigPluginFactory

class BoxConfigPlugin():
    
    def getName(self):
        pass
    
    def execute(self,**kwargs):
        pass



class Plugin(object):
    '''
    classdocs
    '''


    def __init__(self, func):
        self.classref = func
        self.classInstance = func()
        self.pluginfactory = BoxConfigPluginFactory()
        self.register()
        
    def getName(self):
        return self.classInstance.getName()
    
    
    def register(self):
        processorclassname = self.classref.__name__
        if self.getName() is None:
            raise Exception("Plugin name is not defined in plugin config {}".format(processorclassname))
        if not issubclass(self.classref, BoxConfigPlugin):
            raise Exception("Plugin {} not subclass of BoxConfigPlugin".format(processorclassname))
        logging.info("Registering Plugin {}".format(self.getName()))
        self.pluginfactory.registerPlugin(self.getName(), self.classref)
        
    