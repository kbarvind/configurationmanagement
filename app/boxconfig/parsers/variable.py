'''
Created on 19-May-2021

@author: kbarvind
'''


class VariableParser(object):
    '''
    classdocs
    '''

    def __init__(self, config):
        self.config = config
        self.variables = {}
        
    def process(self):
        if 'vars' not in self.config:
            return
        
        self.variables = self.config['vars']
        
    def getVariable(self, key):
        
        if key not in self.variables:
            raise Exception("Variable " + key + " does not exists")
        
        return  self.variables[key]
            
