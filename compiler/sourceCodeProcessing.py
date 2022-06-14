from sys import exit as EXIT

import copy

from compiler.ast import *
from compiler.bytecodeCreation import *

class SyntaxInfoProcessing:
    """
    * Parsing JSON information of symbolInfo *

    Parse the concise symbolinfo written by users into information that can be used directly.
    The Tranquility-Beta version has documentation..
    You can read the documentation, so I won't repeat it here.

    At this time, Syntax Information v1.0-pre version is used.
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
            EXIT(0)

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
            EXIT(0)


    def informationCompletion(self):
        """
        * Complete syntax information *
        In order to facilitate subsequent direct use,
        complete the token attribute of Syntax Information.
        Complete it with Syntax Information allowed attributes,
        That is, set default values for allowed attributes.
        """
        newSyntaxInfo = copy.deepcopy(self.syntaxInfo)
        normalIdentifierPos = 0
        for i in self.syntaxInfo["normalIdentifier"]:
            for l in i.keys():
                if "tokenType" in i[l] and "rangeDirection" in i[l]:
                    if i[l]["tokenType"] == "codeBlock":
                        if "endSymbol" not in i[l]:
                            print("OSError--: Lack of resource intrgrity.")
                            EXIT(0)
                    if "hideSymbol" not in i[l]:
                        newSyntaxInfo["normalIdentifier"][normalIdentifierPos]["hideSymbol"] = "False"
                else:
                    print("OSError$: Lack of resource integrity.")
                    EXIT(0)
            normalIdentifierPos += 1

        self.syntaxInfo = newSyntaxInfo

    def execution(self):
        # Function execution
        self.taskAllocation()
        self.informationCompletion()
        return self.syntaxInfo

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
        comments = None; i = 0
        while len(self.sourceCode) > i:
            if self.sourceCode[i] == '/' and self.sourceCode[i+1] == '/':
                i += 2; comments = "single"
            elif self.sourceCode[i] == '/' and self.sourceCode[i+1] == '*':
                comments = "multiline"
            elif self.sourceCode[i] == '\n' and comments == "single":
                i += 1; comments = None
            elif self.sourceCode[i] == '*' and self.sourceCode[i+1] == '/' and comments == "multiline":
                i += 2; comments = None
            
            if comments == None:
                newCode += self.sourceCode[i]

            i += 1

        self.sourceCode = newCode
        newCode = ''

        # Delete character
        for i in ['\n', '\t', '\t']: self.sourceCode = self.sourceCode.replace(i, '')
    
    def execution(self):
        self.syntaxInfo = SyntaxInfoProcessing(self.syntaxInfo).execution()
        self.deleteUselessSymbol()

        Hurtree(self.sourceCode, self.syntaxInfo).execution()
