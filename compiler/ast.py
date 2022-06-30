from sys import exit as EXIT

class Tree:
    def __init__(self):
        # The code contained in the tree structure
        self.Name   = None 
        # The lexical type of the included code
        self.type   = None
        
        # Branch information of Tree
        self.branchCount = 0
        self.branch      = []

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
        print(self.syntaxInfoPriorityTable)
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
    def __init__(self, sourceCode, syntaxInfoNormalIdentifier, syntaxInfoAdditional, syntaxPriorityNum):
        self.sourceCode                 = sourceCode
        self.syntaxInfoNormalIdentifier = syntaxInfoNormalIdentifier
        self.syntaxInfoAdditional       = syntaxInfoAdditional
        self.syntaxPriorityNum          = syntaxPriorityNum

        self.AST                 = Tree()
        self.tokenPosList        = None
        self.processingCodeTable = {}

        self.referencePosTable   = [0, 0]

    def getProcessingCode(self, tokenPos):
        """
        * Obtain Processing Code based on the location of token *

        tokenPos:
            NO.1 Eelement(Index number 0): The name of token
            NO.2 Eelement: The right position of token
            NO.3 Eelement: The left position of token
            NO.4 Eelement: The information of token
        """
        C = "" # Processing Code

        print(tokenPos)
        if tokenPos[3]["tokenType"] == "sentence":
            C = self.sourceCode[self.referencePos:tokenPos[1]]
            self.referencePos = tokenPos[2]
            print("C:", C)
        elif tokenPos[3]["tokenType"] == "codeBlock":
            symbol = 0
            for p in range(tokenPos[2], len(self.sourceCode)):
                if self.sourceCode[p] == tokenPos[0]: symbol += 1
                elif self.sourceCode[p] == tokenPos[3]["endSymbol"]:
                    if symbol == 0: break
                    else: symbol -= 1
            if not symbol == 0: 
                print("SyntaxError: !!!")
                EXIT(0)
            
            C  = self.sourceCode[self.referencePos:tokenPos[1]]
            C1 = self.sourceCode[tokenPos[2]:p]
            self.referencePos = p + 2 

            print("C:", C)
            print("C1:", C1)

    def ASTCreation(self):
        self.tokenPosList = MarkToken(self.syntaxInfoNormalIdentifier[self.syntaxPriorityNum], 
            self.syntaxInfoAdditional, self.sourceCode).execution()
        
        print(self.tokenPosList)
        
        return self.AST

    def execution(self):
        self.ASTCreation()

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

    Number: 00102726157356b4947396d49474e6f59584a685933526c63697767
    """
    def __init__(self, sourceCode, syntaxInfo):
        self.sourceCode = sourceCode
        self.syntaxInfo = syntaxInfo

        self.ast        = None

    def execution(self):
        self.ast = AstCreation(self.sourceCode, \
            self.syntaxInfo["normalIdentifier"], self.syntaxInfo["additional"], 0).execution()
        return self.ast
