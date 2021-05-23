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
    
    
    
    def uninstall(self):
        
        if not self.checkifalreadyinstalled():
            print("BoxConfig cli is not installed")
            return
            
        command = "pip uninstall -y boxconfig"
        
        response = self.sshservice.executecommand(command)
        
        print("BoxConfig uninstalled Successfully")
        
        
    
    def install(self):
        
        if self.checkifalreadyinstalled():
            print("BoxConfig cli is already installed")
            return 
        self.downloadbootstrap()
        self.makeshellscriptexecutable()
        self.executebootstrap()
    
    
    def downloadbootstrap(self):
        
        command = "mkdir -p /tmp/boxconfig && cd /tmp/boxconfig && rm -rf /tmp/boxconfig/bootstrap.sh && wget -q https://github.com/kbarvind/boxconfig/raw/main/bootstrap.sh"
        
        response = self.sshservice.executecommand(command)
        
        print("Downloaded Bootstrap Script")
        
        
    def makeshellscriptexecutable(self):
        
        command = "chmod 777 /tmp/boxconfig/bootstrap.sh"
        
        response = self.sshservice.executecommand(command)
        
    
    
    def executebootstrap(self):
        
        command = "cd /tmp/boxconfig && ./bootstrap.sh"
        
        response = self.sshservice.executecommand(command)
        
        print("Installed Boxconfig")
        
    def checkifalreadyinstalled(self):
        
        command = "boxconfig --help"
        
        response = self.sshservice.executecommand(command)
        
        tocheck = "command not found"
        
        if tocheck in response.getoutputstring():
            return False
        
        return True
        
        
        
        
        
        
        
    