from json import dumps, loads
import os, sys

import compiler
import interpreter

class SyntaxInfoProcessing:
    """
    * Parsing JSON information of symbolInfo *

    Parse the concise symbolinfo written by users into information that can be used directly.
    The Tranquility-Beta version has documentation.
    You can read the documentation, so I won't repeat it here
    """
    def __init__(self, syntaxInfo):
        self.syntaxInfo          = syntaxInfo
        self.processedSyntaxInfo = {"normalIdentifier": [], "additional":{}}

        self.currentlyIdentifierTable = None
        self.tableGlobalInfomation    = None
        self.taskProcessedSyntaxInfo  = {}
	
    def taskAllocation(self):
        try:
            self.currentlyIdentifierTable = self.syntaxInfo["additional"]
            self.publicInfoProcessing()
            self.processedSyntaxInfo["additional"] = self.currentlyIdentifierTable

            for i in self.syntaxInfo["normalIdentifier"]:
                self.currentlyIdentifierTable = i
                self.publicInfoProcessing()
                self.processedSyntaxInfo["normalIdentifier"].append(self.currentlyIdentifierTable)
        except:
            print("OSError: Lack of resource integrity.")
            sys.exit(0)
    
    def publicInfoProcessing(self):
        try:
            if "global" in self.currentlyIdentifierTable:
                self.tableGlobalInfomation = self.currentlyIdentifierTable["global"]
                self.currentlyIdentifierTable.pop("global")

                # Replace the element in the currently processed identifier tabel
                for i in self.tableGlobalInfomation.keys():
                    for l in self.currentlyIdentifierTable.keys():
                        if not i in self.currentlyIdentifierTable[l]:
                            self.currentlyIdentifierTable[l][i] = self.tableGlobalInfomation[i]
        except:
            print("OSError: Lack of resource integrity.")
            sys.exit(0)

    def execution(self):
	# Function execution
	self.taskAllocation()
        return self.syntaxInfo

class Tranquillity(object):
    def __init__(self):
        # Definition and declaration of variables
        self.osType         = os.name # Computer system type
        self.argvList       = sys.argv # Command parameter list
        self.helpFileNormal = True # Integrity of external resources
        self.cmdInfo        = None # Command parameter information
        self.syntaxInfo     = None
		
        self.sourceCode     = None # Source code to be compiled.
        self.byteCode       = None # Bytecode generated after source code compilation.

        # Function execution
        self.resourcesIntegrity()
        self.argvAnalysis()

    def resourcesIntegrity(self):
        try:
            with open("./doc/resources/cmd.info", "rt") as f:
                self.cmdInfo = f.read()

            with open("./doc/resources/syntaxToken.json") as f:
                self.syntaxInfo = loads(f.read())
        except:
            self.helpFileNormal = False

        if self.helpFileNormal == False:
            print("OSError5: Lack of integrity of external resources.")
            sys.exit(0)
    def argvAnalysis(self):
        with open("./run.ty", "rt") as f: 
            self.sourceCode = f.read()
  
        self.syntaxInfo = SyntaxInfoProcessing(self.syntaxInfo).execution()
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
