import json
import ctypes as C
import os
import subprocess
import py_racf
import r_admin

PY_REXX = os.getenv('PY_RACF_HOME')

class Permit:
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
        self.parms['prof_name'] = ''
        self.parms['class_name'] = ''
        self.parms['flags'] = 0x00000000

        self.racf.log.debug('Permit init')
        if self.func_type is not None:
            self.racf.log.debug('    func_type: (0x%02x)' % self.func_type)
        return

    def set_func_type(self, func_type):
        self.parms['func_type'] = func_type
        return

    def set_prof_name(self, prof_name):
        self.parms['prof_name'] = prof_name
        return

    def set_class_name(self, class_name):
        self.parms['class_name'] = class_name
        return

    #there are 2 different variation of the permit command used so 1 for each
    def run_1(self, rafcomm,prof_name,parms): 
        self.racf.log.debug('Permit run')
        proc = subprocess.run(['./PERMIT.rexx',rafcomm, prof_name,parms],cwd=PY_REXX+'/R_admin/python/REXX',capture_output=True, text = False)
        return proc

    def run_2(self, rafcomm,parms, prof_name,action,cl):
        self.racf.log.debug('Permit run')
        proc = subprocess.run(['./PERMIT2.REXX',rafcomm,parms,prof_name,action,cl],cwd=PY_REXX+'/R_admin/python/REXX',capture_output=True, text = False)
        return proc
