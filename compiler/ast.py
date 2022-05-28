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
        print(self.string)

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

        self.mainAst       = Tree()
        self.endSymbolList = None

        # Token
        self.tokenType = None
        self.tokenEnd  = None
        self.tokenSign = []
    
    def checkResourceIntegrity(self):
        """
        * Check resource integrity. *

        Check if the required resources are missin.
        Note: check the integrity of resources generally.
        """
        try:
            # Statement Terminator
            self.endSymbolList = list(self.syntaxInfo["endSymbol"]["symbolList"])

            if (len(self.endSymbolList) == 0) or (not len(self.endSymbolList) == len(self.syntaxInfo["endSymbol"]["symbolList"])):
                print("OSError2: Lack of resource integrity.")
                sys.exit(0)
        except:
            print("OSError3: Lack of resource integrity.")
            sys.exit(0)

    def getToken(self):
        ...
    
    def buildAST(self):
        ...
    
    def execution(self):
        self.checkResourceIntegrity()
        self.getToken()
