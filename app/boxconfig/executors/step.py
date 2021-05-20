'''
Created on 19-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.pluginfactory import BoxConfigPluginFactory
import sys

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
            plugin = BoxConfigPluginFactory.getPlugin(step.getplugin())
            params = {
                "config" : step.getconfig()
                } 
            try:
                plugin.execute(**params)
            except Exception as ex:
                print(ex)
                sys.exit()   
            