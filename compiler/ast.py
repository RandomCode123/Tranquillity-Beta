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

class AstCreation:
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

    def selectPriority(self):
        tokenList = None
        for i in self.sytnaxInfo["normalIdentifier"]:
            i["additional"] = self.syntaxInfo["additional"]
            tokenList = markToken(i, self.sourceCode).execution()

            # <--

    def execution(self):
        #self.checkResourceIntegrity()
        self.getToken()

class MarkToken:
    """
    Find the location of the specified Token.
    This is equivalent to marking the Token.
    """
    def __init__(self, syntaxInfo, code):
        self.syntaxInfo     = string
        self.code           = targetString

        self.tokenList = []

    def find(self):
        ...

    def execution(self):
        self.find()
        return self.tokenList

class Hurtree:
    """
    * Ast partial boot *
    
    (The following excerpt is from the Tranquility-Beta document.)
    Essentially, hurtree analysis only uses some characteristics 
    wing excerpt is from the tranquility beta document
    brought by token priority to analyze code morphology.
    Syntax information provides the attributes and priority of 
    the token, as well as some other additional attributes,
    and these attributes can help support hurtree's lexical 
    analyzer to parse code lexical and generate corresponding 
    abstract syntax trees.
    """
    def __init__(self, sourceCode, syntaxInfo):
        self.sourceCode = sourceCode
        self.syntaxInfo = syntaxInfo
    
    def prioritySort(self):
        for i in self.syntaxInfo["normalIdentifier"]:
            # print(i)
            ...

    def execution(self):
        self.prioritySort()

