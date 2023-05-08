import chess as ch
import random as rd


class Engine:

    def __init__(self, board, maxDepth, color):
        """
        Inizializza una nuova istanza della classe Engine.

        Args:
        board (chess.Board): un oggetto di tipo chess.Board che rappresenta lo stato corrente del gioco
        maxDepth (int): il massimo numero di mosse a cui l'algoritmo di ricerca può arrivare
        color (str): una stringa, può essere 'b' o 'w', che rappresenta il colore del giocatore che utilizza questa istanza di Engine
        """
        self.board = board
        self.color = color
        self.maxDepth = maxDepth

    def getBestMove(self):
        """
        Chiama il metodo engine() con i parametri None e 1 e ritorna il valore restituito da quest'ultimo.

        Returns:
        chess.Move: la mossa consigliata dall'algoritmo di ricerca
        """
        return self.engine(None, 1)

    def evalFunct(self):
        """
        Calcola e ritorna il punteggio della posizione corrente.

        Il punteggio viene calcolato sommando il valore di ogni pezzo sulla scacchiera, il valore della possibilità di fare scacco matto (se presente) e il valore della fase di apertura.

        Il valore di ogni pezzo viene calcolato dal metodo squareResPoints(), mentre il valore della fase di apertura viene calcolato dal metodo openning(). Inoltre, il metodo aggiunge anche un valore casuale compreso tra 0 e 0.001 per evitare di ottenere sempre lo stesso punteggio per posizioni uguali.

        Returns:
        float: il punteggio della posizione corrente
        """
        compt = 0
        # Calcola il valore di ogni pezzo sulla scacchiera
        for i in range(64):
            compt += self.squareResPoints(ch.SQUARES[i])

        # Aggiunge il valore della possibilità di fare scacco matto e il valore della fase di apertura
        compt += self.mateOpportunity() + self.openning()

        # Aggiunge un valore casuale per evitare di ottenere sempre lo stesso punteggio per posizioni uguali
        compt += 0.001 * rd.random()
        return compt

    def mateOpportunity(self):
        """
        Ritorna 999 se il giocatore che utilizza questa istanza di Engine
        Returns:
        int: il valore della possibilità di fare o subire scacco matto
        """
        if (self.board.legal_moves.count() == 0):
            if (self.board.turn == self.color):
                return -999
            else:
                return 999
        else:
            return 0

    # to make the engine developp in the first moves
    def openning(self):

        """
        Ritorna un valore positivo se il giocatore che utilizza questa istanza di Engine ha il turno e un valore negativo in caso contrario.

        Il valore viene calcolato in base al numero di mosse legali a disposizione del giocatore e alla fase di apertura (prima di aver fatto 10 mosse).

        Returns:
            float: il valore della fase di apertura
        """

        if (self.board.fullmove_number < 10):
            if (self.board.turn == self.color):
                return 1 / 30 * self.board.legal_moves.count()
            else:
                return -1 / 30 * self.board.legal_moves.count()
        else:
            return 0


    def squareResPoints(self, square):
        """
            Ritorna il valore di un pezzo presente nella casella specificata come parametro.

            I valori sono assegnati come segue:
                - pedone: 1
                - cavallo: 3.2
                - alfiere: 3.33
                - torre: 5.1
                - regina: 8.8

            Se il pezzo appartiene al giocatore che utilizza questa istanza di Engine, il valore viene ritornato come valore positivo, altrimenti viene ritornato come valore negativo.

            Args:
                square (chess.Square): la casella di cui si vuole conoscere il valore del pezzo

            Returns:
                float: il valore del pezzo
            """
        pieceValue = 0
        if (self.board.piece_type_at(square) == ch.PAWN):
            pieceValue = 1
        elif (self.board.piece_type_at(square) == ch.ROOK):
            pieceValue = 5.1
        elif (self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue = 3.33
        elif (self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue = 3.2
        elif (self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue = 8.8

        if (self.board.color_at(square) != self.color):
            return -pieceValue
        else:
            return pieceValue

    def engine(self, candidate, depth):

        """
            Algoritmo di ricerca che consiglia la mossa migliore da fare.

            L'algoritmo utilizza il metodo minimax con alpha-beta pruning per esplorare l'albero delle mosse e selezionare la mossa con il miglior punteggio.

            Args:
                candidate (float): il valore attuale del miglior punteggio trovato dall'algoritmo di ricerca
                depth (int): il livello corrente dell'albero delle mosse

            Returns:
                float: il punteggio della mossa consigliata dall'algoritmo di ricerca
            """

        # Se si è raggiunto il massimo numero di profondità o non ci sono più mosse legali, calcola il punteggio della posizione corrente
        if (depth == self.maxDepth
                or self.board.legal_moves.count() == 0):
            return self.evalFunct()

        else:
            # Crea una lista delle mosse legali
            moveListe = list(self.board.legal_moves)

            # Inizializza il nuovo candidato con il valore massimo o minimo possibile a seconda che sia il turno del giocatore o del computer
            newCandidate = None


            if (depth % 2 != 0):
                newCandidate = float("-inf")
            else:
                newCandidate = float("inf")

            # Per ogni mossa legale, esegue la mossa, calcola il punteggio della nuova posizione e aggiorna il candidato
            for i in moveListe:

                # Esegue la mossa i
                self.board.push(i)

                # Calcola il punteggio della nuova posizione
                value = self.engine(newCandidate, depth + 1)

                # Aggiorna il candidato con il punteggio della mossa, se il punteggio è maggiore o minore del candidato attuale a seconda che sia il turno del giocatore o del computer
                if (value > newCandidate and depth % 2 != 0):
                    # Se si è al primo livello dell'albero delle mosse, salva la mossa per poterla ritornare
                    if (depth == 1):
                        move = i
                    newCandidate = value

                elif (value < newCandidate and depth % 2 == 0):
                    newCandidate = value

                # Alpha-beta prunning cuts:
                #   # Se il punteggio della nuova posizione è minore o maggiore del candidato attuale a seconda che sia il turno del giocatore o del computer, annulla la mossa e interrompe il ciclo
                if (candidate != None
                        and value < candidate
                        and depth % 2 == 0):
                    self.board.pop()
                    break
                # (if previous move was made by the human player)
                elif (candidate != None
                      and value > candidate
                      and depth % 2 != 0):
                    self.board.pop()
                    break

                # Annulla la mossa
                self.board.pop()

            # Se non si è al primo livello dell'albero delle mosse, ritorna il candidato
            if (depth > 1):
                return newCandidate
            # Se si è al primo livello dell'albero delle mosse, ritorna la mossa
            else:
                return move