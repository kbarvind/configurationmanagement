'''
Created on 23-May-2021

@author: kbarvind
'''
from builtins import staticmethod

class StringUtils(object):
    '''
    classdocs
    '''

    @staticmethod
    def removenewlinecharacter(line):
        
        line = line.replace('\n','')
        line = line.replace('\t','')
        return line
        