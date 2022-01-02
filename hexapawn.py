import copy
import math


#-------------------------------------------------
#--Purpose: Checks every possible move and evaluates it using minimax
#--Arguments: an array of strings(starting board), size, color of player and the depth limit to search
#--Returns: the optimal move found using minimax (an array of strings or the board state)
#-------------------------------------------------

def hexapawn(startingBoard,sizeOfBoard,color,depthLimit):
    bestScore = -11
    bestMove = None
    currentBoard = HexBoard(startingBoard,color)
    evaluation = currentBoard.evaluateBoard()
    # print(evaluation)
    if(abs(evaluation) == 10 ):
        currentBoard.printBoard()
        print(currentBoard.player, 'win' if evaluation == 10 else 'lose')
        return 'The Game has already been concluded'
        
    if(color == 'w'):
        for move in currentBoard.generateWhiteMoves():
            score = minimax(move, 1, False, depthLimit, 'b')
            if (score > bestScore):
                bestScore = score
                bestMove = move
    else:
        for move in currentBoard.generateBlackMoves():
            score = minimax(move, 1, False, depthLimit, 'w')
            if (score > bestScore):
                bestScore = score
                bestMove = move
    return bestMove.returnArray()


#-------------------------------------------------
#--Purpose:The minimax algorithm that will be called when hexapawn is called
#--Arguments:a HexBoard object, the current depth, maxTurn(Boolean), depthlimit(int), player(char)
#--Returns: an overall evaluation of a move (int)
#-------------------------------------------------
def minimax(currentBoard,currentDepth,maxTurn, depthLimit, player):
    evaluation = currentBoard.evaluateBoard()
    #minimax troubleshooting
    # print('Current depth:', currentDepth)
    # print('Current player:', 'w')
    # currentBoard.printBoard()
    # print(currentBoard.evaluateBoard())
    #First check if game is won or lost
    if(abs(evaluation) == 10 ):
        return evaluation

    #Check if it is the depth limit
    if currentDepth == depthLimit:
        return evaluation
    
    scores = []
    if player == 'w':
        for move in currentBoard.generateWhiteMoves():
            scores.append(minimax(move,currentDepth+1, maxTurn, depthLimit, 'b'))
    else:
        for move in currentBoard.generateBlackMoves():
            scores.append(minimax(move,currentDepth+1, maxTurn, depthLimit, 'w'))
    return max(scores) if maxTurn else min(scores)

#-------------------------------------------------
#--Purpose: A class to store the state of a HexaPawn Board
#--Arguments: takes in a board array and player color 
#--Returns: N/A
#-------------------------------------------------
class HexBoard:
    def __init__(self, board, player ="w"):
        self.board = self.reformatBoard(board)
        self.player = player

    #-------------------------------------------------
    #--Purpose: Reformats an array to suit the class's needs
    #--Arguments: takes in a board array
    #--Returns: returns the formatted board
    #-------------------------------------------------
    def reformatBoard(self, board):
        boardCopy = copy.deepcopy(board)
        formattedBoard =[]
        #changes it to a 2D array instead of an array of strings
        for row in boardCopy:
            formattedRow = []
            for char in row:
                formattedRow.append(char)
            formattedBoard.append(formattedRow)
        return formattedBoard
    
    #-------------------------------------------------
    #--Purpose: Prints the board state in a readable format
    #--Arguments: N/A
    #--Returns:N/A
    #-------------------------------------------------
    def printBoard(self):
        print("Current state:")
        for row in self.board:
            print(row)
        print("Player Color:", self.player)

    #-------------------------------------------------
    #--Purpose: returns the board state as an array of strings
    #--Arguments: N/a
    #--Returns:N/A
    #-------------------------------------------------
    def returnArray(self):
        newArr = []
        for row in self.board:
            newArr.append(''.join(row))
        return newArr

    #-------------------------------------------------
    #--Purpose: This method generates all possible moves for white 
    #--         and returns it as an array of HexBoard objects
    #--Arguments: N/A
    #--Returns: An array of HexBoard Objects
    #-------------------------------------------------
    def generateWhiteMoves(self):
        generatedStates = []
        rowIndex = 0
        for row in self.board:
            charIndex = 0
            for char in row:
                if char == 'w':
                    if(rowIndex < len(self.board)-1):
                        if self.board[rowIndex+1][charIndex] == '-':

                            # copyBoard = copy.deepcopy(self.board)
                            copyBoard = copy.deepcopy(self)
                            copyBoard.board[rowIndex+1][charIndex] = 'w'
                            copyBoard.board[rowIndex][charIndex] = '-'
                            generatedStates.append(copyBoard)

                        if(charIndex < len(row)-1):
                            if self.board[rowIndex+1][charIndex+1] == 'b':
                                copyBoard = copy.deepcopy(self)
                                copyBoard.board[rowIndex+1][charIndex+1] = 'w'
                                copyBoard.board[rowIndex][charIndex] = '-'
                                generatedStates.append(copyBoard)

                        if(charIndex > 0):
                            if self.board[rowIndex+1][charIndex-1] == 'b':
                                copyBoard = copy.deepcopy(self)
                                copyBoard.board[rowIndex+1][charIndex-1] = 'w'
                                copyBoard.board[rowIndex][charIndex] = '-'
                                generatedStates.append(copyBoard)
                charIndex += 1
            rowIndex += 1
        # printBoardArr(generatedStates)
        return generatedStates

    #-------------------------------------------------
    #--Purpose: This method generates all possible moves for black 
    #--         and returns it as an array of HexBoard objects
    #--Arguments: N/A
    #--Returns: An array of HexBoard Objects
    #-------------------------------------------------
    def generateBlackMoves(self):
        generatedStates = []
        rowIndex = 0
        for row in self.board:
            charIndex = 0
            for char in row:
                if char == 'b':
                    if(rowIndex > 0):
                        if self.board[rowIndex-1][charIndex] == '-':
                            copyBoard = copy.deepcopy(self)
                            copyBoard.board[rowIndex-1][charIndex] = 'b'
                            copyBoard.board[rowIndex][charIndex] = '-'
                            generatedStates.append(copyBoard)

                        if(charIndex < len(row)-1):
                            if self.board[rowIndex-1][charIndex+1] == 'w':
                                copyBoard = copy.deepcopy(self)
                                copyBoard.board[rowIndex-1][charIndex+1] = 'b'
                                copyBoard.board[rowIndex][charIndex] = '-'
                                generatedStates.append(copyBoard)

                        if(charIndex > 0):
                            if self.board[rowIndex-1][charIndex-1] == 'w':
                                copyBoard = copy.deepcopy(self)
                                copyBoard.board[rowIndex-1][charIndex-1] = 'b'
                                copyBoard.board[rowIndex][charIndex] = '-'
                                generatedStates.append(copyBoard)
                charIndex += 1
            rowIndex += 1
        return generatedStates


    #-------------------------------------------------
    #--Purpose: Evaluates the static board state as White
    #--Arguments: N/A
    #--Returns: A Number (The evaluation score)
    #-------------------------------------------------
    def evaluateWhite(self):
        boardEval = 0
        rowIndex = 0
        blackPawns = 0
        #---------------------------
        #--Evaluation for white player
        #-- +10 if we won and -10 if we lost
        #-- Else:
        #-- +1 for each white piece
        #-- -1 for each black piece
        #---------------------------
        #First check if we can't move if we can't then we lost
        if not self.generateWhiteMoves():
            return -10
        #Then Check if your opponent cant move
        elif not self.generateBlackMoves():
            return 10
        else:
            #Next iterate through the board 
            for row in self.board:
                charIndex = 0
                for char in row:
                    #Check for white piece
                    if char == 'w':
                        #Check if we won with the piece on the other side
                        if(rowIndex==len(self.board)-1):
                            return 10
                        #Else that means we have a piece 
                        else:
                            boardEval+=1
                    #Next Check for black pieces
                    elif char == 'b':
                        #Return a loss if black won
                        if(rowIndex==0):
                            return -10
                        #else minus 1 since black has a piece
                        else:
                            boardEval-=1
                            blackPawns += 1
                    charIndex += 1
                rowIndex += 1
            #Check number of opponents pawns since no pawns is a win
            if blackPawns == 0:
                return 10
            return boardEval

    #-------------------------------------------------
    #--Purpose: Evaluates the static board state as Black
    #--Arguments: N/A
    #--Returns: A Number (The evaluation score)
    #-------------------------------------------------
    def evaluateBlack(self):
        boardEval = 0
        rowIndex = 0
        whitePawns = 0
        #---------------------------
        #--Evaluation for white player
        #-- +10 if we won and -10 if we lost
        #-- Else:
        #-- -1 for each white piece
        #-- +1 for each black piece
        #---------------------------
        #First check if we can't move if we can't then we lost
        if not self.generateBlackMoves():
            return -10
        #Then Check if your opponent cant move
        elif not self.generateWhiteMoves():
            return 10
        else:
            #Next iterate through the board 
            for row in self.board:
                charIndex = 0
                for char in row:
                    #Check for black pawns
                    if char == 'b':
                        #Check if we won with the piece on the other side
                        if(rowIndex==0):
                            return 10
                        #Else that means we have a piece 
                        else:
                            boardEval+=1
                    #Next Check for white pawns
                    elif char == 'w':
                        #Return a loss if white won
                        if(rowIndex==len(self.board)-1):
                            return -10
                        #else minus 1 since white has a piece
                        else:
                            boardEval-=1
                            whitePawns +=1
                    charIndex += 1
                rowIndex += 1
            #Check number of opponents pawns since no pawns is a win
            if whitePawns == 0:
                return 10
            return boardEval

    #-------------------------------------------------
    #--Purpose: Since the board evaluation will always be the negative of the other
    #--         this function just evaluates for white and returns whatever color is needed
    #--Arguments: The Player color if specified
    #--Returns: A number (evaluation according to the color)
    #-------------------------------------------------
    def evaluateBoard(self):
        if(self.player == 'w'):
            boardEval = self.evaluateWhite()
            return boardEval
        else:
            boardEval = self.evaluateBlack()
            return boardEval


        

#-------------------------------------------------
#--Purpose: Code to print an array of board objects
#--Arguments: an Array
#--Returns: N/A
#-------------------------------------------------
def printBoardArr(array):
    print("----Array Start----")
    for board in array:
        board.printBoard()
    print("----Array End----")


#Testing Grounds
whiteOnly = ["www","---","---"]
blackOnly = ["----","----","----","bbbb"]
draw4x4 = ["w-w-","bwbw","-b--","---b"]
draw3x3 = ["-w-","wbw","b-b"]
fresh4x4 = ["wwww","----","----","bbbb"]
test1 = ['----', 'wbww', '-bb-', '---b']

currentMove = fresh4x4
currentMove=hexapawn(currentMove,3,'b',5)
print(currentMove)




