'''
Created on 20-May-2021

@author: kbarvind
'''
from app.boxconfig.plugin.plugindecorator import BoxConfigPlugin, Plugin
from app.utils.os.osinformation import OSInfo
from app.boxconfig.executors.process import NativeProcessRequest, \
    NativeProcessExecutor
from app.boxconfig.model.exception import StepExecutionException
from app.boxconfig.model.response import StepExecutionResponse


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
            raise StepExecutionException("package-apt can be applied only for linux debian platform")
        
        linuxdistribution = list(OSInfo.getPlatformLinuxDistribution())
        
        if len(linuxdistribution) == 0:
            StepExecutionResponse.getSuccessResponse("Skipping since plugin can only be applied to debian or ubuntu")
            return
        
        distribution = linuxdistribution[0].lower()
        
        if distribution != 'ubuntu' and distribution != 'debian':
            StepExecutionResponse.getSuccessResponse("Skipping since plugin can only be applied to debian or ubuntu")
            return
        
        state = config['state']
        package = config['package']
        
        if state == 'install':
            multipackageinstallation = False
        
            if isinstance(package, list):
                multipackageinstallation = True
            
            if not multipackageinstallation:
                return self.install(package)
            else:
                packages = package
                stepresponse = StepExecutionResponse.getSuccessMultiResponse()
                for packagename in packages:
                    response = self.install(packagename)
                    stepresponse.addResponse(response)
                return stepresponse
        else:
            raise StepExecutionException("State " + state + " is not valid")
    
    def isalreadyinstalled(self, package):
        
        response = self.executecommand("apt -qq list " + package)
        
        print("Is installed")
        print(response.getstdout())
        if len(response.getstdout()) == 0:
            return False
        else:
            return True
    
    def install(self, package):
        
        if self.isalreadyinstalled(package):
            return StepExecutionResponse.getSuccessResponse("Package " + package + " already installed")
        
        response = self.executecommand("apt-get -y update && apt-get -y install " + package)
        
        if response.getcontainsexception():
            raise StepExecutionException("Error while installing package " + package + " : " + response.getexception())
        
        if response.getreturncode() != 0:
            raise StepExecutionException("Error while installing package " + package + " : " + response.getstderr())
        
        return StepExecutionResponse.getSuccessResponse("Package " + package + " successfully installed", description=response.getstdout())
    
    def executecommand(self, command):
        
        nativeprocessrequest = NativeProcessRequest()
        nativeprocessrequest.setcommand(command)
        
        native_process_executor = NativeProcessExecutor(nativeprocessrequest)
        try:
            response = native_process_executor.execute()
            return response
        except:
            raise Exception("Error while executing command")
        
    def validate(self, config):
        
        if 'package' not in config:
            raise StepExecutionException("Package Name configuration is not available in configuration")
        
        if 'state' not in config:
            raise StepExecutionException("State configuration is not available in configuration")
