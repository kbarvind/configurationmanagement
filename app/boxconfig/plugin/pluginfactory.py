'''
Created on 20-May-2021

@author: kbarvind
'''
from builtins import staticmethod

class BoxConfigPluginFactory(object):
    '''
    classdocs
    '''


    registry = {}
    plugins = []
    
    @staticmethod
    def registerPlugin( pluginname, plugin):
        if pluginname in BoxConfigPluginFactory.registry:
            raise Exception("Plugin {} already exists".format(pluginname))
        BoxConfigPluginFactory.registry[pluginname] = plugin
        BoxConfigPluginFactory.plugins.append(pluginname)
    
    @staticmethod 
    def getPlugin( pluginname):
        if pluginname not in BoxConfigPluginFactory.plugins:
            raise Exception("Plugin {} does not exists".format(pluginname))
        return BoxConfigPluginFactory.registry[pluginname]()
    
    @staticmethod
    def getPlugins():
        return BoxConfigPluginFactory.plugins