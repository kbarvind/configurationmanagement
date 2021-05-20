'''
Created on 20-May-2021

@author: kbarvind
'''

class BoxConfigPluginFactory(object):
    '''
    classdocs
    '''


    plugins = []
    registry = {}

    def __init__(self):
        self.registry = {}
        self.plugins = []
    
    def registerPlugin(self, pluginname, plugin):
        if pluginname in self.registry:
            raise Exception("Plugin {} already exists".format(pluginname))
        self.registry[pluginname] = plugin
        self.plugins.append(pluginname)
        
    def getPlugin(self, pluginname):    
        if pluginname not in self.registry:
            raise Exception("Plugin {} does not exists".format(pluginname))
        return self.registry[pluginname]()
    
    def getPlugins(self):
        return self.plugins