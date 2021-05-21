'''
Created on 21-May-2021

@author: kbarvind
'''


class StepExecutionException(Exception):
    '''
    classdocs
    '''

    def __init__(self, message, exeception=None):
        self.message = message
        self.exception = exeception
        super().__init__(self.message)
        
    def getexception(self):
        return self.exception
    
    def getmessage(self):
        return self.message
        
    
        
