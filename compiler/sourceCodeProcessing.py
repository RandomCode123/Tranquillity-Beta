from compiler.ast import *
from compiler.bytecodeCreation import *

class SourceCodeProcessing:
    """
    * Analyze the source code, Parse source code into bytes. *

    First, parse the code into a AST according to the syntax token.
    And now, At this time, the AST can be parsed into bytecode.
    Parse the bytecode according to AST.
    """
    def __init__(self, sourceCode, syntaxInfo):
        # Definition and declaration of variables
        self.sourceCode = sourceCode
        # Grammatical structur
        self.syntaxInfo = syntaxInfo
        
        # AST tree struct
        self.simpleAstTree = {}
        self.astTree       = {}
        
    def deleteUselessSymbol(self):
        """
        * Delete useless characters *

        Before parsing the sourcme code,
        First delete the characters written by the user in the source code that are useless for parsing.
        """
        newCode = '' # New code after being processed

        # Delete comments
        comments = None; i=0
        while len(self.sourceCode) > i:
            if self.sourceCode[i] == '/' and self.sourceCode[i+1] == '/':
                i += 2
                comments = "single"
            elif self.sourceCode[i] == '/' and self.sourceCode[i+1] == '*':
                comments = "multiline"
            elif self.sourceCode[i] == '\n' and comments == "single":
                i += 1
                comments = None
            elif self.sourceCode[i] == '*' and self.sourceCode[i+1] == '/' and comments == "multiline":
                i += 2
                comments = None
            
            if comments == None:
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
        self.deleteUselessSymbol()
        astCreation(self.sourceCode, self.syntaxInfo).execution()
