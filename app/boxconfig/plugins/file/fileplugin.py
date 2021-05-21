'''
Created on 20-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import Plugin, BoxConfigPlugin
from app.utils.os.file import File
import os
from app.utils.os.osinformation import OSInfo

@Plugin
class FilePlugin(BoxConfigPlugin):
    '''
    classdocs
    '''
    
    def getName(self):
        return "file"


    def execute(self, **kwargs):
        config =  kwargs.get('config', {})
        self.validate(config)
        if config['state'] == 'create':
            self.createfile(config)
    
    
    def createfile(self,config):
        path = config['path']
        
        fileexists = File.checkIfPathExists(path)
        
        if fileexists:
            print("File "+path+" already available so skipping")
            return
        
        mode = None
        
        if 'mode' in config:
            mode = config['mode']
        
        
        if mode == "folder":
            if File.checkIfPathExists(path):
                print("Skipping: Directory already exists in path "+path)
                return
            os.makedirs(path,parents=True, exist_ok=True)
        else:
            try:
                File.touch(path)
            except Exception as ex:
                print(ex)
                raise Exception("Could not create file in path "+path)
        
        
        
    def validate(self,config):
        
        if 'state' not in config:
            raise Exception("State is not available for executing file plugin")
        
        if 'path' not in config:
            raise Exception("Path is not available for executing file plugin")
            
        