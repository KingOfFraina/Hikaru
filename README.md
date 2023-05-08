# Hikaru
This is a Python chess engine that uses the minimax algorithm with alpha-beta pruning to evaluate the best moves.

The class Engine in ChessEngine.py has the following methods:

   - **\_\_init\_\_ (self, board, maxDepth, color)**: initializes a new instance of the class Engine with the current board state, the maximum depth of the search algorithm, and the color of the player using this instance;
   - **getBestMove(self)**: calls the engine() method with parameters None and 1 and returns the move suggested by the search algorithm;
   - **evalFunct(self)**: calculates and returns the score of the current position based on the value of each piece on the board, the potential for checkmate, and the opening phase;
    - **mateOpportunity(self)**: returns 999 if the player using this instance of Engine has the potential for checkmate, -999 if the opponent has the potential, and 0 otherwise;   
   - **openning(self)**: returns a positive value if the player using this instance of Engine is in the opening phase (i.e., has fewer than 10 moves) and has legal moves available and a negative value if the opponent is in the opening phase and has legal moves available. Returns 0 otherwise; 
 - **squareResPoints(self, square)**: returns the value of a piece on the specified square based on the type of piece and the player who owns it;   
  - **engine(self, candidate, depth)**: the main algorithm that uses minimax with alpha-beta pruning to search the game tree and return the best move.
  
Overall, this code provides a solid foundation for a chess engine, but there are some areas where it could be improved. For example, the **squareResPoints()** method assigns fixed values to each piece, which may not be accurate in all situations. Additionally, the **openning()** method only considers the number of legal moves available, but it may be more informative to also consider the position of the pieces on the board. Finally, the **mateOpportunity()** method only looks at the current state of the board, but it may be more accurate to also consider future moves that could lead to checkmate.
