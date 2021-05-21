'''
Created on 20-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import Plugin, BoxConfigPlugin
from app.utils.os.file import File
import os
from app.utils.os.osinformation import OSInfo
from app.boxconfig.model.response import StepExecutionResponse
from app.boxconfig.model.exception import StepExecutionException

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
            return self.createfile(config)
        else:
            return StepExecutionResponse.getErrorResponse("State "+config['state']+" not valid")
    
    
    def createfile(self,config):
        path = config['path']
        
        fileexists = File.checkIfPathExists(path)
        
        if fileexists:
            return StepExecutionResponse.getSuccessResponse("File "+path+" already available so skipping")
        
        mode = None
        
        if 'mode' in config:
            mode = config['mode']
        
        
        if mode == "folder":
            if File.checkIfPathExists(path):
                return StepExecutionResponse.getSuccessResponse("Skipping: Directory already exists in path "+path)
            os.makedirs(path, exist_ok=True)
            return StepExecutionResponse.getSuccessResponse("Successfully created folder in "+path)
        else:
            try:
                File.touch(path)
                return StepExecutionResponse.getSuccessResponse("Successfully created file "+path)
            except Exception as ex:
                raise StepExecutionException("Could not create file in path "+path,exeception=ex)
        
        
        
    def validate(self,config):
        
        if 'state' not in config:
            raise StepExecutionException("State is not available for executing file plugin")
        
        if 'path' not in config:
            raise StepExecutionException("Path is not available for executing file plugin")
            
        