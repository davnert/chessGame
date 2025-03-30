class game:

    def __init__(self, player1, player2, gameType, increment):
        self.gameType = gameType
        self.player1 = player1
        self.player2 = player2
        self.time = 0
        self.increment = increment
        self.turn = ""
        self.moves = 1

        if gameType == "rapid":
            self.time=10
        elif (gameType == "blitz"):
            self.time=5
        elif (gameType == "bullet"):
            self.time=2        

    # Klocka börjar --> var spelare har individuell klocka
    # Klockan stannar när ett drag har spelats och det är motståndarend drag. --> bör kunnd uppdatera en bolean och stanna klockan och spara dess state.
    # Visualizera tiden på skärmen i realtid.
    
    """ 
    What data structure is best for constucting pieces and what attributes do they have Pieces have:

    1. type --> easily assigned
    2. position --> connected with the board position coordinaate --> not to hard to assign.
    3. color --> Either white or black --> easily assigned
    4. Moving restriction --> available moving squares for the piece --> harder to assign.
          -   If pinned it should not be able to move.
          -   If same color piece on a possible available path, it should not be able to move to that/thoose squares.
          -   The hoeses might be tricky, as they can jump over pieces.

   """
    def instantiate_pieces():
        pass
        
    def startGame(self):
        pass


    def update_piece_position(self):
        if self.move % 2 != 0:
            # wite to move
            pass
        else:
            # black to move
            pass
    