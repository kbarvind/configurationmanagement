'''
Created on 16-Mar-2020

@author: kbarvind
'''
import importlib
import sys
import pkgutil
from builtins import staticmethod

class ModuleUtils():
    
    @staticmethod
    def loadModules(module):
        path_list = []
        spec_list = []
        for importer, modname, ispkg in pkgutil.walk_packages(module.__path__):
            import_path = f"{module.__name__}.{modname}"
            if ispkg:
                spec = pkgutil._get_spec(importer, modname)
                importlib._bootstrap._load(spec)
                spec_list.append(spec)
            else:
                path_list.append(import_path)
        for spec in spec_list:
            del sys.modules[spec.name]
        
        for path in path_list:
            __import__(path, globals(), locals())
    