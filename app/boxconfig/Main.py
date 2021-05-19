'''
Created on 19-May-2021

@author: kbarvind
'''
from app.utils.os.file import File, FileHandler
from app.utils.yaml.parse import YamlParser
from app.boxconfig.parsers.variable import VariableParser
from app.boxconfig.parsers.steps import StepParser
from app.boxconfig.executors.step import StepExecutor


class BoxConfig(object):
    '''
    classdocs
    '''

    def __init__(self, filepath):
        self.file = filepath
        self.filecontent = None
        self.configyaml = None
        self.init()
        self.parseyaml()
        
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
    
    def parseyaml(self):
        try:
            yamlParser = YamlParser()
            self.configyaml = yamlParser.parser(self.file)
        except Exception as ex:
            raise Exception("Error while parsing yaml file from " + self.file + " : " + str(ex)) from None
    
    def process(self):
        
        variableparser = VariableParser(self.configyaml)
        variableparser.process()
        
        stepparser = StepParser(self.configyaml)
        stepparser.process()
        
        stepexecutor = StepExecutor(stepparser)
        stepexecutor.process()
