'''
Created on 23-May-2021

@author: kbarvind
'''

class SSHResponse():
    
    def __init__(self):
        self.output = None
        self.error = None
        
        
    def setoutput(self, output):
        self.output = output
    
    
    def getoutput(self):
        return self.output
    
    def seterror(self, error):
        self.error = error
        
    def geterror(self):
        return self.error

class SSHConnector(object):
    '''
    classdocs
    '''

    def init(self):
        
        self.hostname = None
        self.ispassword = False
        self.issshkey = False
        self.username = None
        self.password = None
        self.sshkey = None
        self.client = None

    def getconnector(self):
        pass
    
    def connect_execute(self):
        pass
    
    def executecommand(self, command, commandinput = None):
        pass
    
    def transferfile(self, source, destination):
        pass
    
    def downloadfile(self, source, destination):
        pass
    
    def connect(self, **kwargs):
        
        self.hostname = kwargs.get('hostname', self.hostname)
        self.username = kwargs.get('username', self.username)
        self.password = kwargs.get('password', self.password)
        self.sshkey = kwargs.get('sshkey', self.sshkey)
        
        if self.hostname is None:
            raise Exception(" Hostname is not provided")
        
        if self.username is None:
            raise Exception("ssh user name is not provided")
        
        if self.password is None and self.sshkey is None:
            raise Exception("ssh password or sshkey is not provided")
        
        if self.password is not None:
            self.ispassword = True
        else:
            self.issshkey = True
        
        self.connect_execute()