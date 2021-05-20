'''
Created on 20-May-2021

@author: kbarvind
'''
import subprocess
from app.utils.os.osinformation import OSInfo
from sys import stdin, stderr, stdout


class NativeProcessRequest():
    
    command = None
    failsilently = False
    ignoreoutput = False
    environment = {}
    timeout = None
    path = None
    cwd = None
    stdout = subprocess.PIPE
    stderr = subprocess.PIPE
    
    def setcwd(self, cwd):
        self.cwd = cwd
        
    def getcwd(self):
        return self.cwd
    
    def setstdout(self, stdout):
        self.stdout = stdout
        
    def getstdout(self):
        return self.stdout
    
    def setstderr(self, stderr):
        self.stderr = stderr
        
    def getstderr(self):
        return self.stderr
    
    def settimeout(self, timeout):
        self.timeout = timeout
        
    def gettimeout(self):
        return self.timeout
    
    def setpath(self, path):
        self.path = path
        
    def getpath(self):
        return self.path
    
    def setcommand(self, command):
        self.command = command
        
    def getcommand(self):
        return self.command
    
    def setfailsilently(self, failsilently):
        self.failsilently = failsilently
    
    def getfailsilently(self):
        return self.failsilently
    
    def setignoreoutput(self, ignoreoutput):
        self.ignoreoutput = ignoreoutput
    
    def getignoreoutput(self):
        return self.ignoreoutput
    
    def setenvironment(self, environment):
        self.environment = environment
        
    def getenvironment(self):
        return self.environment



class NativeProcessResponse():
    
    stdout = None
    stderr = None
    returncode = None
    exception = None
    containsexception = False
    
    def setcontainsexception(self,containsexception):
        self.containsexception = containsexception
        
    def getcontainsexception(self):
        return self.containsexception
    
    def setexception(self,exception):
        self.containsexception = True
        self.exception = exception
        
    def getexception(self):
        return self.exception
    
    def setstdout(self,stdout):
        self.stdout = stdout
        
    def getstdout(self):
        return self.stdout
    
    def setstderr(self,stderr):
        self.stderr = stderr
        
    def setretuencode(self, returncode):
        self.returncode = returncode
        
    def getreturncode(self):
        return self.returncode
    

class NativeProcessExecutor(object):
    '''
    classdocs
    '''

    def __init__(self, request):
        self.request = request
        self.response = NativeProcessResponse()
        
    def execute(self):
        
        command = self.request.getcommand()
        environ = self.request.getenvironment()
        environ['PATH'] = OSInfo.getPATHEnvironemnt()
        timeout = self.request.gettimeout()
        path = self.request.getpath()
        try:
            if path is not None:
                pathString = OSInfo.getPathVariableSeprator().join(path)
                environ['PATH'] = environ['PATH'] + OSInfo.getPathVariableSeprator() + pathString
                
            self.process = subprocess.Popen(
                command,
                shell=True,
                universal_newlines=True,
                env=environ,
                cwd=self.request.getcwd(),
                stdout=self.request.getstdout(),
                stderr=self.request.getstderr(),
                stdin=subprocess.PIPE,
            )
            stdout, stderr = self.process.communicate(input=stdin, timeout=timeout)
            self.response.setstdout(stdout)
            self.response.setstderr(stderr)
            self.response.setretuencode(self.process.returncode)
        except OSError as exc:
            self.response.setexception("Exception in command execution {}".format(str(exc)))
        
        return self.response