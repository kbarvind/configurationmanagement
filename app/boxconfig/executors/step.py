'''
Created on 19-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.pluginfactory import BoxConfigPluginFactory
import sys
from app.boxconfig.model.exception import StepExecutionException
from app.boxconfig.model.response import StepExecutionResponse

class StepExecutor(object):
    '''
    classdocs
    '''


    def __init__(self, stepparser):
        self.stepparser = stepparser
        
    def process(self, **kwargs):
        
        steps = self.stepparser.getsteps()
        
        for step in steps:
            print("-----------------------------------------------")
            print("Executing step with plugin "+step.getplugin())
            
            plugin = BoxConfigPluginFactory.getPlugin(step.getplugin())
            params = {
                "config" : step.getconfig()
                }
            
            for key, value in kwargs.items():
                params[key] = value
            
            try:
                response = plugin.execute(**params)
                if not isinstance(response, StepExecutionResponse):
                    print("Response from plugin "+step.getplugin()+" is not instance of StepExecutionResponse")
                    sys.exit()
                self.processresponse(response, step)
            except StepExecutionException as stepexception:
                print(">> Error: "+str(stepexception))
                sys.exit()
            except Exception as ex:
                print(ex)
                sys.exit()   
    
    
    def processresponse(self, responses, step):
        if not responses.getismultiresponse():
            self.printresponse(responses)
        else:
            for response in responses.getresponses():
                if not isinstance(response, StepExecutionResponse):
                    print("One of Response from  "+step.getplugin()+" is not instance of StepExecutionResponse")
                    sys.exit()
                self.printresponse(response)
    
    def printresponse(self, response):
        print(">> "+response.getOutput())
        if response.getdescription() is not None:
            print("")
            print(response.getdescription())
                
            
