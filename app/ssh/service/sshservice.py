'''
Created on 23-May-2021

@author: kbarvind
'''
from app.ssh.connector.connectorfactory import SSHConnectorFactory


class SSHService(object):
    '''
    classdocs
    '''

    def __init__(self, connector, hostname, username, password=None):
        self.connector = connector
        self.hostname = hostname
        self.username = username
        self.password = password
        
    def getParameters(self):
        
        return {
                "hostname" : self.hostname,
                "username" : self.username,
                "password" : self.password
            }
        
    def executecommand(self, command):
        
        connector = SSHConnectorFactory.getConnector(self.connector)
        
        try:
            connector.connect(**self.getParameters())
        except Exception as ex:
            print(ex)
            raise Exception("Could not connect to host " + self.hostname + " with username " + self.username) from None
        
        try:
            return connector.executecommand(command)
        except Exception as ex:
            print(ex)
            raise Exception("Error while executing command " + command) from None
        
        
