from os import name as SYSTEM_TYPE
from sys import exit as EXIT
from sys import argv as ARGV
from json import loads

import compiler
import interpreter

class Tranquillity(object):
    def __init__(self):
        # Definition and declaration of variables
        self.osType         = SYSTEM_TYPE # Computer system type
        self.argvList       = ARGV # Command parameter list
        self.helpFileNormal = True # Integrity of external resources
        self.cmdInfo        = None # Command parameter information
        self.syntaxInfo     = None # Syntax information
        
        self.sourceCode     = None # Source code to be compiled.
        self.byteCode       = None # Bytecode generated after source code compilation.

        # Function execution
        self.resourcesIntegrity()
        self.argvAnalysis()

    def resourcesIntegrity(self):
        try:
            with open("./resources/cmd.info", "rt") as f:
                self.cmdInfo = f.read()

            with open("./resources/syntaxToken.json") as f:
                self.syntaxInfo = loads(f.read())
        except:
            self.helpFileNormal = False

        if self.helpFileNormal == False:
            print("OSError5: Lack of integrity of external resources.")
            EXIT(0)
    def argvAnalysis(self):
        with open("./run.ty", "rt") as f: 
            self.sourceCode = f.read()
        self.sourceCode += ' '
  
        self.bytecode   = compiler.Compiler(self.sourceCode, self.syntaxInfo).execution()

# For later running on the command line .ty program preparation
"""
if len(argvList) == 1:
    # The user has not entered any information at this time.
    print(cmdInfo)
    sys.exit(0)
"""

if __name__ == "__main__":
    Tranquillity()
