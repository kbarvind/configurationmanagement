'''
Created on 19-May-2021

@author: kbarvind
'''

class StepParser(object):
    '''
    classdocs
    '''

    def __init__(self, config, variableparser=None):
        self.config = config
        self.variableparser = variableparser
        self.steps = []
        
    def process(self):
        
        if 'steps' not in self.config:
            raise Exception("Steps is not provided in config")
        
        self.stepconfigs = self.config['steps']
        
        for stepconfig in self.stepconfigs:
            step = Step(stepconfig)
            self.steps.append(step)
        
        print("Configurations contains "+str(len(self.steps))+" steps")
        
    def getsteps(self):
        return self.steps



class Step():
    
    def __init__(self, step, variableparser=None):
        self.step = step
        self.variableparser = variableparser
        self.plugin = None
        self.config = None
        self.validate()
        self.addConfig()
    
    
    def getplugin(self):
        return self.plugin
        
    def validate(self):
        if 'plugin' not in self.step:
            raise Exception("Plugin is not provided in one of the step")
        
        self.plugin = self.step['plugin']
        
    
    def addConfig(self):
        if 'config' not in self.step:
            return 
        self.config = self.step['config']
        
    def getconfig(self):
        return self.config
        
        
        
