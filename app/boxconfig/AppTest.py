'''
Created on 23-May-2021

@author: kbarvind
'''
from app.ssh.service.sshservice import SSHService
from app.boxconfig.boot.install import BoxConfigInstallation


def testssh():
    
    connector = "paramiko"
    hostname1 = "34.229.84.240"
    hostname2 = "54.227.102.186"
    username = "root"
    password = "E6MVMOVVFLND77YAJAGTOGPP"
    
    
    installation = BoxConfigInstallation(hostname1,username,password)
    installation.executebootstrap()

if __name__ == '__main__':
    testssh()