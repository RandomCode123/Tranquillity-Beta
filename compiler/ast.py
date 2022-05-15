class Tree:
    def __init__(self):
        """
        Initialize tree.
        """
        # The code contained in the tree structure
        self.code   = None 
        # The lexical type of the included code
        self.type   = None
        
        self.branchCount = 0
        self.branch      = []

    def set(self, code, type):
        """
        Set basic data in tree.
        """
        self.code = code
        self.type = type

    def addBranch(self, tree):
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
    def __init__(self, sourceCode):
        self.mainAst = Tree()
    
    def getToken(self):
        ...

class astSytnaxChecking:
    def __init__(self):
        ...
