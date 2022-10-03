"""
import chess as ch

board = ch.Board() #create a chess board instance
board.legal_moves #returns a dynamic list of legal moves
board.legal_moves.count() #returns how many legal moves
board.push(move) #play a move (transform the state of the board)
board.pop() #removes the last move played
board.piece_type_at(square) #returns the square'scorresponding ch piec object
board.turn #returns a ch color object

"""

import chess as ch

class Engine():
    def __init__(self, board, maxDepth, color):
        self.board = board
        self.maxDepth = maxDepth
        self.color = color

    def engine(self, candidate, depth):
