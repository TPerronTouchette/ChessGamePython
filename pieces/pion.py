
from pieces.piece import Piece

class Pion(Piece):
    def __init__(self, equipe, position:tuple = (-1,-1)):
        super().__init__(position, equipe)
        self.premierMouvement = True

    def mon_type(self) -> str:
        return 'Pion'

    def deplacement(self, nouvellePosition):
        super().deplacement(nouvellePosition)
        self.premierMouvement = False

    #TODO Doit retourner une liste de liste des mouvements possibles dans chaque direction (une pour les mouvements et l'autre pour l'attaque
    def getMouvement(self) -> list[list[tuple[int,int]]]:
        return [[(-1, -1)]]