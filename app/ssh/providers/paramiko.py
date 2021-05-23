'''
Created on 23-May-2021

@author: kbarvind
'''
from app.ssh.connector.connector import SSHConnector, SSHResponse
from paramiko.client import SSHClient
import paramiko
from sys import stdout, stdin


class ParamikoSSHProvider(SSHConnector):
    '''
    classdocs
    '''

    def getconnector(self):
        return "paramiko"
    
    def connect_execute(self):
        
        if not self.ispassword:
            raise Exception("SSH Key Support is not available ")
        
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.hostname, username=self.username, password=self.password)
        
    def executecommand(self, command, commandinput=None):
        
        stdin, stdout, stderr = self.client.exec_command(command)
        
        if commandinput is not None:
            stdin.write(commandinput + "\n")
            
        sshresponse = SSHResponse()
        sshresponse.setoutput(stdout.readlines())
        sshresponse.seterror(stderr.readlines())
        
    def transferfile(self, source, destination):
        
        try:
            ftpclient = self.client.open_sftp()
            ftpclient.put(source, destination)
        except Exception as ex:
            raise ex
        finally:
            ftpclient.close()
    
    
    def downloadfile(self, source, destination):
        
        try:
            ftpclient = self.client.open_sftp()
            ftpclient.put(source, destination)
        except Exception as ex:
            raise ex
        finally:
            ftpclient.close()
        
