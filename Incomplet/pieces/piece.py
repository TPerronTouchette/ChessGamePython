# --------------------------------------------------------------------------------------------------------
# Chess with PyGame
# Created by Martin Blore 2023
# Full explanation can be found at https://codewithmartin.io/articles/how-to-code-a-chess-game-in-python
# --------------------------------------------------------------------------------------------------------


class Piece:

    def __init__(self, position:tuple = (-1,-1), equipe:str = 'None'):
        self.equipe = equipe
        self.position = position
        self.premierMouvement = False


    def mon_type(self) -> str:
        return 'Piece'

    #Cette méthode doit nous dire si other est une piece ennemi
    def is_enemy_piece(self, other):
        if (other.equipe == 'None'):
            return False
        if(self.equipe != other.equipe):
            return True

        return False
    #Est utilise dans perform_Move
    def deplacement(self, nouvellePosition):
        self.position = nouvellePosition



    #Cette methode doit retourner une liste de liste de mouvements possibles pour la piece
    def getMouvement(self) -> list[list[tuple[int, int]]]:
        return [[self.position]]

    #Operateur !=
    def __ne__(self, other) -> bool:
        return self.mon_type() + self.equipe != other.mon_type() + other.equipe
    #Operateur ==
    def __eq__(self, other) -> bool:
        return not (self != other)

