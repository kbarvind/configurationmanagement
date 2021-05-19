'''
Created on 19-May-2021

@author: kbarvind
'''
from app.utils.os.file import File, FileHandler
from app.utils.yaml.parse import YamlParser


class BoxConfig(object):
    '''
    classdocs
    '''

    def __init__(self, filepath):
        self.file = filepath
        self.filecontent = None
        self.configyaml = None
        self.init()
        
    def init(self):
        try:
            File.checkIfFIleExists(self.file)
        except Exception:
            raise Exception("File path " + self.file + " does not exists") from None
        
        try:
            File.checkIsFile(self.file)
        except Exception:
            raise Exception("File " + self.file + " does not exists") from None
        
        try:
            filehandler = FileHandler()
            self.filecontent = filehandler.readFile(self.file)
        except Exception:
            raise Exception("Error while reading file from " + self.file) from None
        
        try:
            yamlParser = YamlParser()
            self.configyaml = yamlParser.parser(self.file)
        except Exception:
            raise Exception("Error while parsing yaml file from " + self.file) from None
        
        
    
    def process(self):
        
        print(self.configyaml)
    
    
