'''
Created on 23-May-2021

@author: kbarvind
'''
from builtins import staticmethod
from app.ssh.providers.paramiko import ParamikoSSHProvider


class SSHConnectorFactory(object):
    '''
    classdocs
    '''

    @staticmethod
    def getConnector(connectorname):
        
        if connectorname == "paramiko":
            return ParamikoSSHProvider()
        
        raise Exception("Connector " + connectorname + " is not supported")
        
