'''
Created on 19-Apr-2020

@author: kbarvind
'''
from builtins import staticmethod
import yaml



class YamlParser():
    
    
    @staticmethod
    def parser(filepath: str):
        
        with open(filepath,"r") as file:
            return yaml.load(file, Loader=yaml.FullLoader)
        

            