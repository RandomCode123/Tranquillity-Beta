from compiler.sourceCodeProcessing import *

class Compiler:
	def __init__(self, sourceCode, syntaxInfo):
		# Definition and declaration of variables
		self.sourceCode = sourceCode
		self.syntaxInfo = syntaxInfo
		
		self.bytecode   = None
		
	def basicProcessing(self):
		# Basic processing of source code
		self.bytecode = SourceCodeProcessing(self.sourceCode, self.syntaxInfo).execution()
	
	def execution(self):
		# Function execution
		self.basicProcessing()
