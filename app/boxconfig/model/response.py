'''
Created on 21-May-2021

@author: kbarvind
'''
from builtins import staticmethod

class StepExecutionResponse(object):
    '''
    classdocs
    '''


    def __init__(self, description=None):
        self.iserror = False
        self.output = ""
        self.error = ""
        self.responses = []
        self.multioutput = False
        self.description = description
        
    @staticmethod
    def getSuccessMultiResponse():
        response = StepExecutionResponse()
        response.setIsError(False)
        response.multioutput = True
        return response
    
    @staticmethod
    def getSuccessResponse(output, description=None):
        response = StepExecutionResponse()
        response.setIsError(False)
        response.setOutput(output)
        if description is not None:
            response.description = description
        return response
        
    @staticmethod
    def getErrorResponse(error, description=None):
        response = StepExecutionResponse()
        response.setIsError(True)
        response.setOutput(error)
        if description is not None:
            response.description = description
        return response
    
    def getismultiresponse(self):
        return self.multioutput
    
    def getdescription(self):
        return self.description
    
    
    def getIsError(self):
        return self.iserror
    
    def setIsError(self, iserror):
        self.iserror = iserror
    
    
    def getOutput(self):
        return self.output
    
    def setOutput(self, output):
        self.output = output
        
        
    def addResponse(self, response):
        self.responses.append(response)
        
    def setError(self, error):
        self.error = error
        
    def getError(self):
        return self.error