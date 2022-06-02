import sys

class Tree:
    def __init__(self):
        # The code contained in the tree structure
        self.code   = None 
        # The lexical type of the included code
        self.type   = None
        
        # Branch information of Tree
        self.branchCount = 0
        self.branch      = []

    def set(self, code, type):
        """
        * Set basic data in tree. *
        """
        self.code = code
        self.type = type

    def addBranch(self, tree):
        """
        * Create a new branch *
        In essence, "create" is to add a new Tree to the branch list.
        """
        self.branch.append(tree)
        self.branchCount += 1

def showTree(mainTree):
    print('=' * 20)
    print("The id of the Tree:", id(mainTree))
    print("The code of the Tree: \n"+'-'*5+'\n'+str(mainTree.code)+'\n'+'-'*5)
    print("The type of the Tree: "+str(mainTree.type))
    print("The id of the Tree included: ", end='')
    for i in mainTree.branch:
        print(id(i), end='')
    print("\n"+'='*20)

class markToken:
    """
    Find the location of the specified Token.
    This is equivalent to marking the Token.
    """
    def __init__(self, string, targetString):
        self.string           = string
        self.targetString     = targetString

        self.position         = [] # Location of token
    
    def find(self):
        stringMode      = False 
        targetStringPos = 0

        for i in range(len(self.string)):
            # Enter string mode.
            # In string mode, no specified token is recognized.
            if self.string[i] == '"' or self.string[i] == '\'':
                if stringMode == False:
                    stringMode = self.string[i] 
                elif self.string[i] == stringMode: 
                    stringMode = False
            # Find the token and mark it if it's not in string mode.
            if stringMode == False and self.targetString[targetStringPos] == self.string[i]: 
                for j in range(len(self.targetString)):
                    if self.targetString[j] != self.string[i+j]:
                        i += j
                        break
                self.position = [i, i+len(self.targetString)] # Mark the Token
                break

    def execution(self):
        self.find()
        return self.position

class astCreation:
    """
    * Creation of a preliminary AST structure *
    
    Parse the source code into AST.
    Token the source code through the token information.
    Then, it is parsed step by step through the token tag.
    Gradually improve ast from overall to detailed.
    """
    def __init__(self, sourceCode, syntaxInfo):
        self.sourceCode = sourceCode
        self.syntaxInfo = syntaxInfo

        self.mainAst       = {}
        self.endSymbolList = None

        # Token
        self.tokenType      = None
        self.tokenHiding    = None
        self.rangeDirection = None
        self.endSymbol      = None

        self.frontmostIdentifierPos = [-1, -1]
        self.endSymbolIdentifierPos = None
        self.frontmostIdentifier    = None

    def getToken(self):
        # print("0:", self.syntaxInfo["normalIdentifier"][0])
        codeToBeProcessed      = self.sourceCode
        for i in self.syntaxInfo["normalIdentifier"]:
            while codeToBeProcessed != '':
                for l in i.keys():
                    pos = markToken(codeToBeProcessed, l).execution()

                    # If it cannot be found, the loop is restarted.
                    # The meaning is to find the identifier in the identifier table of the same priority
                    if pos == []: continue
                    # Find the top identifier in the code position in the same priority table
                    if pos[0] >= self.frontmostIdentifierPos[0]:
                        self.frontmostIdentifier    = l
                        self.frontmostIdentifierPos = pos

                        try:
                            # Get identifier information
                            self.tokenType      = i[l]["type"]
                            self.tokenHiding    = i[l]["tokenHiding"]
                            if "endSymbol" in i[l]:
                                self.endSymbol  = i[l]["endSymbol"]
                                # If there is an endsymbol attribute,
                                # then mark the position of endsymbol.
                                self.endSymbolIdentifierPos = \
                                    markToken(codeToBeProcessed, self.endSymbol).execution()
                            self.rangeDirection = i[l]["rangeDirection"]
                        except:
                            print("OSError: Lack of integrity of external resources.")
                            sys.exit(0)
                # Tag dependent spanning Tree
                self.buildAST()
                # Reload the code to be parsed
                codeToBeProcessed = self.sourceCode

    def buildAST(self):
        ...
    
    def execution(self):
        #self.checkResourceIntegrity()
        self.getToken()
