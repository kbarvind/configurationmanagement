'''
Created on 21-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import Plugin, BoxConfigPlugin
from app.boxconfig.executors.process import NativeProcessRequest, \
    NativeProcessExecutor


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
            self.start(service)
        else:
            raise Exception("Action " + action + " not supported")
    
    def start(self, service):
        
        command = "systemctl start " + service
        response = self.executecommand(command)
        
        response.printresponse()
        
        if response.getcontainsexception():
            raise Exception("Error while starting service " + service + " : " + response.getexception())
        
        if response.getreturncode() != 0:
            print(response.getstdout())
            raise Exception("Error while starting service " + service + " : " + response.getstderr())
        
        
        print("Service " + service + " started")
    
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
        
