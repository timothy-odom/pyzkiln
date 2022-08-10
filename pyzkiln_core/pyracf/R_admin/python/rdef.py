import json
import ctypes as C
import os
import subprocess
import r_admin

PY_REXX = os.getenv('PY_RACF_HOME')

class Rdef:
    def __init__(self, racf=None, radmin=None, func_type=None):
        self.func_type = func_type

        if racf is not None:
            self.racf = racf
        else:
            print('Error - missing ancestor object')
            raise Exception

        if radmin is not None:
            self.radmin = radmin
        else:
            print('Error - missing ancestor object')
            raise Exception

        self.parms = {}
        self.parms['func_type'] = func_type
        self.parms['params'] = ''
        self.parms['prof_name'] = ''
        self.parms['class_name'] = ''
        self.parms['flags'] = 0x00000000

        self.racf.log.debug('Rdef init')
        if self.func_type is not None:
            self.racf.log.debug('    func_type: (0x%02x)' % self.func_type)
        return

    def set_func_type(self, func_type):
        self.parms['func_type'] = func_type
        return

    def set_params(self, params):
        self.parms['params'] = params
        return

    def set_prof_name(self, prof_name):
        self.parms['prof_name'] = prof_name
        return

    def set_class_name(self, class_name):
        self.parms['class_name'] = class_name
        return
    
    def get_func_type(self):
        return self.parms['func_type']

    def get_prof_name(self):
        return self.parms['prof_name']

    def get_class_name(self):
        return self.parms['class_name']

    def get_params(self):
        return self.parms['params']

    def run(self,prof_name,params):
        self.racf.log.debug('RDEF run')

        proc = subprocess.run(['./RDEF.REXX',prof_name,params],cwd=PY_REXX+'/R_admin/python/REXX',capture_output=True,text=False)
        return proc
