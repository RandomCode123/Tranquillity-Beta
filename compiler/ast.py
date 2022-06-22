from lib2to3.pgen2 import token


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

class MarkToken:
    """
    Find the location of the specified Token.
    This is equivalent to marking the Token.
    """
    def __init__(self, syntaxInfoPriorityTable, syntaxInfoAdditionalTable, code):
        self.syntaxInfoPriorityTable     = syntaxInfoPriorityTable
        self.syntaxInfoAdditionalTable   = syntaxInfoAdditionalTable
        self.code                        = code

        self.tokenList = []

    def find(self):
        for key in self.syntaxInfoPriorityTable.keys():
            for i in range(len(self.code)):
                if self.code[i] == key[0]:
                    found = True
                    for l in range(len(key)):
                        try:
                            if key[l] != self.code[i+l]:
                                found = False
                                break
                        except:
                            found = False
                            break

                    if found == True: self.tokenList.append([key, i, i+len(key), self.syntaxInfoPriorityTable[key]])
                    i += l - 1

    def sort(self, pos):
        if(len(pos)<=1):
            return pos
        mid = int(len(pos)/2)
        leftList, rightList = self.sort(pos[:mid]), self.sort(pos[mid:])

        result = []; i = 0; j = 0
        while i < len(leftList) and j < len(rightList):
            if rightList[j][1] < leftList[i][1]:
                result.append(rightList[j])
                j += 1
            else:
                result.append(leftList[i])
                i += 1
                
        result += leftList[i:]+rightList[j:]
        return result

    def execution(self):
        self.find()
        self.tokenList = self.sort(self.tokenList)
        return self.tokenList

class AstCreation:
    """
    * Creation of a preliminary AST structure *

    Parse the source code into AST.
    Token the source code through the token information.
    Then, it is parsed step by step through the token tag.
    Gradually improve ast from overall to detailed.
    """
    def __init__(self, sourceCode, tokenList):
        self.sourceCode = sourceCode
        self.tokenList  = tokenList

        self.AST                 = Tree()
        self.processingCodeTable = {}

    def getProcessingCode(self):
        for i in self.tokenList:
            ... # <--

    def ASTCreation(self):
        MarkToken()

    def execution(self):
        ...

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

        self.ast        = Tree()
    
    def prioritySort(self):
        code = self.sourceCode
        for i in self.syntaxInfo["normalIdentifier"]:
            print(i)
            tokenPosList = MarkToken(i, self.syntaxInfo["additional"], code).execution()
            print(tokenPosList)
            AST          = AstCreation(code, tokenPosList).execution()
            # showTree(AST)

            break # <--

    def execution(self):
        self.prioritySort()

