'''
Created on 22-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import Plugin, BoxConfigPlugin
from app.boxconfig.model.exception import StepExecutionException
from app.utils.os.file import File
from app.boxconfig.model.response import StepExecutionResponse
import shutil


@Plugin
class FileCopy(BoxConfigPlugin):
    '''
    classdocs
    '''


    def getName(self):
        return "filecopy"
    
    def execute(self, **kwargs):
        filedirectory = kwargs.get('filedirectory', {})
        config =  kwargs.get('config', {})
        self.validate(config)
        
        filename = config['name']
        destination = config['destination']
        
        allfiles = File.getFilesinDirectory(filedirectory+"/files")
        
        filespec = None
        
        for file in allfiles:
            if filename == file['file']:
                filespec = file['fullpath']
                break
        
        if filespec is None:
            raise StepExecutionException("File "+filename+" not present in boxconfig configuration directory")
        
        
        if not File.checkIsDir(destination):
            raise StepExecutionException("Destination directory "+destination+" does not exists")
        
        
        try:
            shutil.copy(filespec, destination)
        except Exception as ex:
            StepExecutionException("Could not copy file to "+destination, exeception=ex)
        
        return StepExecutionResponse.getSuccessResponse("File copied successfully to "+destination)
        
    
    
    def validate(self, config):
        
        if 'name' not in config:
            raise StepExecutionException("File name to copy is not provided")
        
        if 'destination' not in config:
            raise StepExecutionException("Destination Path is not provided")
        
        