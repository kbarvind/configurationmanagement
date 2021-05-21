'''
Created on 21-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import Plugin, BoxConfigPlugin
from app.boxconfig.executors.process import NativeProcessRequest, \
    NativeProcessExecutor
from app.boxconfig.model.response import StepExecutionResponse
from app.boxconfig.model.exception import StepExecutionException


@Plugin
class Service(BoxConfigPlugin):
    '''
    classdocs
    '''

    def getName(self):
        return "service"
    
    def execute(self, **kwargs):
        config = kwargs.get('config', {})
        
        action = config['action']
        service = config['service']
        
        if action == 'start':
            return self.start(service)
        else:
            raise StepExecutionException("Action " + action + " not supported")
        
        
    def isrunning(self, service):
        
        command = "systemctl status " + service
        response = self.executecommand(command)
        
        if response.getcontainsexception():
            False
            
        if response.getreturncode() != 0:
            False
            
        return True
        
    
    def start(self, service):
        
        if self.isrunning(service):
            return StepExecutionResponse.getSuccessResponse("Skipping Service "+service+" is already running")
            
        
        command = "systemctl start " + service
        response = self.executecommand(command)
        
        
        if response.getcontainsexception():
            raise StepExecutionException("Error while starting service " + service + " : " + response.getexception())
        
        if response.getreturncode() != 0:
            raise StepExecutionException("Error while starting service " + service + " : " + response.getstderr())
        
        
        return StepExecutionResponse.getSuccessResponse("Service " + service + " started", description=response.getstdout())
    
    def executecommand(self, command):
        
        nativeprocessrequest = NativeProcessRequest()
        nativeprocessrequest.setcommand(command)
        
        native_process_executor = NativeProcessExecutor(nativeprocessrequest)
        try:
            response = native_process_executor.execute()
            return response
        except:
            raise Exception("Error while executing command")
        
    def validate(self, config):
        
        if 'name' not in config:
            raise Exception("Service name is not available in configuration")
        
        if 'action' not in config:
            raise Exception("Service action is not available in configuration")
        
