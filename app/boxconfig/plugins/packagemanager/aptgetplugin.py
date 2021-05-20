'''
Created on 20-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import BoxConfigPlugin, Plugin
from app.utils.os.osinformation import OSInfo

@Plugin
class AptGetPlugin(BoxConfigPlugin):
    '''
    classdocs
    '''


    def getName(self):
        return "package-apt"
    
    
    def execute(self, **kwargs):
        config =  kwargs.get('config', {})
        
        if OSInfo.getPlatformSystem() != 'linux':
            raise Exception("package-apt can be applied only for linux debian platform")
        
        print(OSInfo.getPlatformLinuxDistribution())