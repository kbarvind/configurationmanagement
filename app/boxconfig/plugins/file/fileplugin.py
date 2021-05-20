'''
Created on 20-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import Plugin, BoxConfigPlugin

@Plugin
class FilePlugin(BoxConfigPlugin):
    '''
    classdocs
    '''
    
    def getName(self):
        return "file"


    def execute(self, **kwargs):
        print("Executing File Plugin")
        