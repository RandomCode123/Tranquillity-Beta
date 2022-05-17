from json import dumps, loads
import os, sys

import compiler
import interpreter

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
	
		self.bytecode = compiler.Compiler(self.sourceCode, self.syntaxInfo)
"""
if len(argvList) == 1:
	# The user has not entered any information at this time.
	print(cmdInfo)
	sys.exit(0)
"""
if __name__ == "__main__":
	Tranquillity()
