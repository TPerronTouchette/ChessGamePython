
from pieces.piece import Piece

class Cavalier(Piece):
    def __init__(self, equipe, position:tuple = (-1,-1)):
        super().__init__(position, equipe)

    def mon_type(self) -> str:
        return 'Cavalier'

    #TODO Doit retourner une liste de liste des mouvements possibles dans chaque direction
    def getMouvement(self) -> list[list[tuple[int,int]]]:
        return [[(-1, -1)]]
