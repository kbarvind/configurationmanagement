'''
Created on 23-May-2021

@author: kbarvind
'''
from app.ssh.service.sshservice import SSHService

class BoxConfigInstallation(object):
    '''
    classdocs
    '''


    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.sshservice = SSHService("paramiko",self.hostname,self.username,password=self.password)
    
    
    
    def downloadbootstrap(self):
        
        command = "mkdir -p /tmp/boxconfig && cd /tmp/boxconfig && rm -rf /tmp/boxconfig/bootstrap.sh && wget -q https://github.com/kbarvind/boxconfig/raw/main/bootstrap.sh"
        
        response = self.sshservice.executecommand(command)
        
        print(response.getoutputstring())
        print(response.geterrorstring())
        
        
    def makeshellscriptexecutable(self):
        
        command = "chmod 777 /tmp/boxconfig/bootstrap.sh"
        
        response = self.sshservice.executecommand(command)
        
        print(response.getoutputstring())
        print(response.geterrorstring())
    
    
    def executebootstrap(self):
        
        command = "cd /tmp/boxconfig && ./bootstrap.sh"
        
        response = self.sshservice.executecommand(command)
        
        print(response.getoutputstring())
        print(response.geterrorstring())
        
        
        
        
        
    