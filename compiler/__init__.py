from compiler.sourceCodeProcessing import *

class Compiler:
	def __init__(self, sourceCode, syntax):
		# Definition and declaration of variables
		self.sourceCode = sourceCode
		self.syntax     = syntax
		
		self.bytecode   = None
		
		# Function execution
		self.basicProcessing()
	def basicProcessing(self):
		""" Basic processing of source code """
		self.bytecode = SourceCodeProcessing(self.sourceCode, self.syntax)
