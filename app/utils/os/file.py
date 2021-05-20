'''
Created on 07-Mar-2020

@author: kbarvind
'''
import os
import sys
from builtins import staticmethod
import json

class File(object):
    '''
    classdocs
    '''

    @staticmethod
    def getFilesinDirectory(dir_path,file_extension=None):
        
        File.log.info("searching for : "+file_extension+" in folder path "+dir_path)
        if File.checkIfPathExists(dir_path) == False:
            raise Exception("Path "+dir_path+" does not exists")
        
        if File.checkIsDir(dir_path) == False:
            raise Exception("Path "+dir_path+" is not directory")
            
        
        files = []
        for r, d, f in os.walk(dir_path):
            for file in f:
                toAppend = False
                if file_extension is not None:
                    if file_extension in file:
                        toAppend = True
                else:
                    toAppend = True
                    
                if toAppend == True:
                    file = {
                        "root" : r.replace(dir_path,""),
                        "file" : file,
                        "fullpath" : os.path.join(r, file)
                        }
                    files.append(file)
        
        return files
    
    @staticmethod
    def checkIsFile(filePath):
        return os.path.isfile(filePath)

    @staticmethod
    def checkIsDir(dirPath):
        return os.path.isdir(dirPath)

    @staticmethod
    def checkIfPathExists(path):
        return os.path.exists(path)
    
    @staticmethod
    def getRootDir():
        return os.path.dirname(sys.modules['__main__'].__file__)
    
    
    @staticmethod
    def get_config_files():
        root_dir = File.getRootDir()
        print(root_dir)
        
    @staticmethod
    def remove_file(filepath):
        File.checkIfFIleExists(filepath)
        os.remove(filepath)
    
        
    @staticmethod
    def checkIfFIleExists(path: str):
        if not File.checkIfPathExists(path):
            raise Exception("Path {} does not exists".format(path))
        
        if not File.checkIsFile(path):
            raise Exception("File {} does not exists".format(path))
        
        return True
    
        
        
        
class FileHandler():
    
    def readFile(self,filepath):
        try:
            file = open(filepath,"r")
            return file.read()
        except Exception as ex:
            raise Exception("Exception while trying to read file from "+filepath+" : "+str(ex))
        
    def write(self,filepath,file_content):
        try:
            file = open(filepath,"w")
            file.writelines(file_content)
            file.close()
            return True
        except Exception as ex:
            raise Exception("Exception while trying to read file from "+filepath+" : "+str(ex))
    

        
    