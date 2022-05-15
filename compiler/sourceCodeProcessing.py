from compiler.ast import *
from compiler.bytecodeCreation import *

class SourceCodeProcessing:
    """
    * Analyze the source code, Parse source code into bytes. *
    
    First, parse the code into a AST according to the syntax token.
    And now, At this time, the AST can be parsed into bytecode.
    Parse the bytecode according to AST.
    """
    def __init__(self, sourceCode, syntax):
		# Definition and declaration of variables
        self.sourceCode = sourceCode
        # Grammatical structur
        self.syntax     = syntax
		
        # AST tree struct
        self.simpleAstTree = Tree()
        self.astTree       = Tree()
		
    def deleteUselessSymbol(self):
        """
        * Delete useless characters *

        Before parsing the source code,
        First delete the characters written by the user in the source code that are useless for parsing.
        """
        newCode = ''

        # Delete annotation
        annotation = None

        i=0
        while len(self.sourceCode) > i:
            if self.sourceCode[i] == '/' and self.sourceCode[i+1] == '/':
                i += 2
                annotation = "single"
            elif self.sourceCode[i] == '/' and self.sourceCode[i+1] == '*':
                annotation = "multiline"
            elif self.sourceCode[i] == '\n' and annotation == "single":
                i += 1
                annotation = None
            elif self.sourceCode[i] == '*' and self.sourceCode[i+1] == '/' and annotation == "multiline":
                i += 2
                annotation = None
            
            if annotation == None:
                newCode += self.sourceCode[i]

            i += 1

        self.sourceCode = newCode
        newCode = ''

        # Delete character
        for i in ['\n', '\t', '\t']: self.sourceCode = self.sourceCode.replace(i, '')

        symbol  = True # Whether the character currently processed is the character after the statement terminator.	
        for i in self.sourceCode:
            if i == ';':
                symbol = True   
            if i != ' ' or symbol == False: 
                newCode += i
            if i != ' ' and symbol == True: 
                symbol = False

        self.sourceCode = newCode
    
    def execution(self):
        # Function execution
        self.deleteUselessSymbol()

        astCreation()
