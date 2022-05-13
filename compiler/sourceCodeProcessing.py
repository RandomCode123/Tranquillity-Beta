from compiler.astBuild import *
from compiler.bytecodeBuild import *

class SourceCodeProcessing:
    def __init__(self, sourceCode, syntax):
        """
        Parse the source code.
        """
		# Definition and declaration of variables
        self.sourceCode = sourceCode
        # Grammatical structur
        self.syntax     = syntax
		
        # AST tree struct
        self.simpleAstTree = Tree()
        self.astTree       = Tree()
		
		# Function execution
        self.deleteUselessSymbol()
        self.pretreatment()
		
    def deleteUselessSymbol(self):
        """ Delete useless characters """
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
	
    def pretreatment(self):
        """
        Source code preprocessing.
        Simple lexical analysis of the code,
        get specific code blocks.
        """
        print(self.sourceCode)
        self.simpleAstTree.set("ROOT", "token")

        pretreatmentCode = ""
        codeBlockSymbol  = 0
        currentLevelTree = None
        
        print()
        pos = 0
        while len(self.sourceCode) > pos:
            if self.sourceCode[pos] == '{': 
                codeBlockSymbol += 1
            if self.sourceCode[pos] == '}':
                codeBlockSymbol -= 1

            if (self.sourceCode[pos] == '}' and codeBlockSymbol == 0) or (self.sourceCode[pos] == ';' and codeBlockSymbol == 0):
                print(pretreatmentCode)
                pretreatmentCode += self.sourceCode[pos]

                currentLevelTree = Tree()
                codeStructTree   = Tree()

                codeStructTree.set(pretreatmentCode, "code")
                currentLevelTree.set(self.sourceCode[pos], "token")
                currentLevelTree.addBranch(codeStructTree)

                pretreatmentCode = ""; pos += 1
            else:
                pretreatmentCode += self.sourceCode[pos]
                pos += 1

        showTree(self.simpleAstTree)
