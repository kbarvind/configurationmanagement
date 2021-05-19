'''
Created on 19-May-2021

@author: kbarvind
'''

class StepExecutor(object):
    '''
    classdocs
    '''


    def __init__(self, stepparser):
        self.stepparser = stepparser
        
    def process(self):
        
        steps = self.stepparser.getsteps()
        
        for step in steps:
            print("Executing step with plugin "+step.getplugin())