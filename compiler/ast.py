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

class astCreation:
    """
    * Creation of a preliminary AST structure *
    
    Parse the source code into AST.
    Token the source code through the token information.
    Then, it is parsed step by step through the token tag.
    Gradually improve ast from overall to detailed.
    """
    def __init__(self, sourceCode, syntaxInfo):
        self.syntaxInfo = syntaxInfo

        self.mainAst       = Tree()
        self.endSymbolList = None
    
    def checkResourceIntegrity(self):
        """
        * Check resource integrity. *

        Check if the required resources are missing,
        """
        try:
            self.endSymbolList = list(self.syntaxInfo["endSymbol"])

            if (not "priority" in self.endSymbolList) or (len(self.endSymbolList) == 0) or (not len(self.endSymbolList)-1 == len(self.syntaxInfo["endSymbol"]["priority"])):
                    print("OSError: Lack of resource integrity.")
                    sys.exit(0)
        except:
            print("OSError: Lack of resource integrity.")
            sys.exit(0)

    def getToken(self):
        print(self.syntaxInfo)
    
    def execution(self):
        self.checkResourceIntegrity()
        self.getToken()

class astSytnaxChecking:
    def __init__(self):
        ...
