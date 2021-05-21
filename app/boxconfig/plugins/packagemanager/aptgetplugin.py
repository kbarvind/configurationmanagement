'''
Created on 20-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import BoxConfigPlugin, Plugin
from app.utils.os.osinformation import OSInfo
from app.boxconfig.executors.process import NativeProcessRequest, \
    NativeProcessExecutor
from _struct import pack


@Plugin
class AptGetPlugin(BoxConfigPlugin):
    '''
    classdocs
    '''

    def getName(self):
        return "aptget"
    
    def execute(self, **kwargs):
        config = kwargs.get('config', {})
        self.validate(config)
        
        if OSInfo.getPlatformSystem() != 'linux':
            raise Exception("package-apt can be applied only for linux debian platform")
        
        linuxdistribution = list(OSInfo.getPlatformLinuxDistribution())
        
        if len(linuxdistribution) == 0:
            print("Skipping since plugin can only be applied to debian or ubuntu")
            return
        
        distribution = linuxdistribution[0].lower()
        
        if distribution != 'ubuntu' and distribution != 'debian':
            print("Skipping since plugin can only be applied to debian or ubuntu")
            return
        
        state = config['state']
        package = config['package']
        
        if state == 'install':
            self.install(package)
        else:
            raise Exception("State " + state + " is not valid")
    
    
    def isalreadyinstalled(self,package):
        
        response = self.executecommand("apt -qq list " + package)
        
        if len(response.getstdout()) == 0:
            return False
        else:
            return True
        
    
    
    def install(self, package):
        
        if self.isalreadyinstalled(package):
            print("Package "+package+" already installed")
            return
        
        response = self.executecommand("apt-get -y update && apt-get -y install " + package)
        
        if response.getcontainsexception():
            raise Exception("Error while installing package " + package + " : " + response.getexception())
        
        
        if response.getreturncode() != 0:
            print(response.getstdout())
            raise Exception("Error while installing package " + package + " : " + response.getstderr())
        
        print(response.getstdout())
    
    def executecommand(self, command):
        
        nativeprocessrequest = NativeProcessRequest()
        nativeprocessrequest.setcommand(command)
        
        native_process_executor = NativeProcessExecutor(nativeprocessrequest)
        try:
            response =  native_process_executor.execute()
            return response
        except:
            raise Exception("Error while executing command")
        
    def validate(self, config):
        
        if 'package' not in config:
            raise Exception("Package Name configuration is not available in configuration")
        
        if 'state' not in config:
            raise Exception("State configuration is not available in configuration")
