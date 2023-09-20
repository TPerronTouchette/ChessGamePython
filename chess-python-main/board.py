# --------------------------------------------------------------------------------------------------------
# Chess with PyGame
# Created by Martin Blore 2023
# Full explanation can be found at https://codewithmartin.io/articles/how-to-code-a-chess-game-in-python
# --------------------------------------------------------------------------------------------------------
import math

import pygame

from board_render import BoardRender
#from piece_moves import PieceMoves
from move_result import MoveResult
from pieces.piece import Piece
from pieces.roi import Roi
from pieces.reine import Reine
from pieces.fou import Fou
from pieces.cavalier import Cavalier
from pieces.tour import Tour
from pieces.pion import Pion

class Board:
    def __init__(self):
        self.board = [[Piece((i, j)) for j in range(8)] for i in range(8)]

        '''
        Board indexes for reference:

        0,0 	0,1     0,2     0,3     0,4     0,5     0,6     0,7
        1,0     1,1     1,2     1,3     1,4     1,5     1,6     1,7
        2,0     2,1     2,2     2,3     2,4     2,5     2,6     2,7
        3,0     3,1     3,2     3,3     3,4     3,5     3,6     3,7
        4,0     4,1     4,2     4,3     4,4     4,5     4,6     4,7
        5,0     5,1     5,2     5,3     5,4     5,5     5,6     5,7
        6,0     6,1     6,2     6,3     6,4     6,5     6,6     6,7
        7,0     7,1     7,2     7,3     7,4     7,5     7,6     7,7
        '''

        self.cell_size = 100
        self.board_start_x = 100
        self.board_start_y = 100
        self.hide_row_index = -1
        self.hide_col_index = -1
        self.white_square_color = (230, 230, 230)
        self.black_square_color = (100, 150, 100)
        self.start_drag_square = (-1, -1)
        self.dragging_piece = Piece()




        self.last_moved_piece = Piece()
        self.last_moved_piece_from = (0,0)
        self.last_capture_piece = Piece()
        self.was_first_move = False

    # Clears the board.
    def clear(self):
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                self.board[row_index][col_index] = Piece()

    # Set up the board state for a new game.
    def setup(self):
        self.clear()
        self.setup_standard()
        #self.setup_stale_mate()

    # Causes the specific square to not be drawn, used for when drag operations are happening.
    def hide_square(self, row, col):
        self.hide_row_index = row
        self.hide_col_index = col

    # Unhides the hidden square.
    def unhide_square(self):
        self.hide_row_index = -1
        self.hide_col_index = -1

    # Draw the board and pieces.
    def draw(self, screen, images):
        BoardRender.draw_board(self, screen)
        BoardRender.draw_pieces(self, screen, images)

    # Gets the current board square that the mouse cursor is over.
    def board_index_from_mouse_pos(self):
        mouse_pos = pygame.mouse.get_pos()

        grid_x = mouse_pos[0] - self.board_start_x
        grid_y = mouse_pos[1] - self.board_start_y

        clicked_in_grid = True

        if (grid_x < 0 or grid_y < 0):
            clicked_in_grid = False

        if (grid_x > self.cell_size * 8 or grid_y > self.cell_size * 8):
            clicked_in_grid = False

        if (clicked_in_grid):
            col_index = math.floor(grid_x / self.cell_size)
            row_index = math.floor(grid_y / self.cell_size)

            return (row_index, col_index)
        else:
            return (-1, -1)

    def is_piece_on_square(self, row, col):
        return self.board[row][col] != Piece()

    def start_drag(self, row, col):
        self.hide_square(row, col)
        self.start_drag_square = row, col
        self.dragging_piece = self.board[row][col]

    def stop_drag(self):
        self.unhide_square()
        self.dragging_piece = Piece()

    #Permet d'annuler le dernier mouvement
    def undo_move(self):
        positionDebut = self.last_moved_piece_from
        positionFin = self.last_moved_piece.position

        self.last_moved_piece.position = positionDebut
        self.last_capture_piece.position = positionFin

        self.last_moved_piece.premierMouvement = self.was_first_move

        self.board[positionDebut[0]][positionDebut[1]] = self.last_moved_piece
        self.board[positionFin[0]][positionFin[1]] = self.last_capture_piece



    # When a piece has been dragged, and its the correct players turn, the piece movement
    # on the board needs to be validated.
    def perform_move(self, end_square):
        #Si on ne tient pas une vrai piece, alors on sort de la fonction
        if self.dragging_piece == Piece():
            return False

        start_square = self.start_drag_square
        piece = self.dragging_piece

        moves = self.filtre(piece)

        #si end_square n'est pas un mouvement alors on n'effectue pas le mouvement
        if not end_square in moves:
            return False

        # Record this move.
        self.last_moved_piece = piece
        self.last_moved_piece_from = start_square
        self.last_capture_piece = self.board[end_square[0]][end_square[1]] # la piece qui se trouve a end_square
        self.was_first_move = piece.premierMouvement

        # Perform the piece move.
        self.board[start_square[0]][start_square[1]] = Piece()
        self.board[end_square[0]][end_square[1]] = piece
        piece.deplacement(end_square)
        return True

    """TODO
    Determiner le type de la piece et appeler une méthode de filtre
    en fonction de la piece qui permet de savoir la liste des mouvements
    valide.
    """
    def filtre(self, piece) -> list[tuple[int,int]]:
        return [(-1, -1)]
    #Nous permet de filtrer les positions accessibles a partir de sa position
    def filtrePieceSurChemin(self, mouvements:list, piece):
        for i in range(len(mouvements)):
            y = mouvements[i][0]
            x = mouvements[i][1]
            if self.board[y][x].equipe != 'None': #une vrai piece
                if self.board[y][x].is_enemy_piece(piece) == True:
                    if len(mouvements) != 1:
                        for k in range(i + 1, len(mouvements)):
                            mouvements.pop()
                else:
                    for k in range(i, len(mouvements)):
                        mouvements.pop(i)
                break

    #Nous permet de filtrer les positions qui sont dans le plateau
    def filtrePieceSurJeu(self, piece) -> list[list]:
        temporaire = piece.getMouvement()
        mouvements = []
        for i in range(len(temporaire)):
            listeTemp = []
            for j in range(len(temporaire[i])):
                if temporaire[i][j][0] < 0 or temporaire[i][j][1] < 0 \
                        or temporaire[i][j][0] > 7 or temporaire[i][j][1] > 7:
                    continue
                else:
                    listeTemp.append(temporaire[i][j])
            if len(listeTemp) != 0:
                mouvements.append(listeTemp)

        return mouvements



    def filtrePion(self, piece:Pion) -> list[tuple[int,int]]:

        mouvementValides = []

        mouvements = self.filtrePieceSurJeu(piece)

        #la premiere sous-liste est pour le mouvement du pion
        self.filtrePieceSurChemin(mouvements[0], piece)
        if len(mouvements[0]) != 0 and piece.is_enemy_piece(self.board[mouvements[0][-1][0]][mouvements[0][-1][1]]):
            mouvements[0].pop()

        mouvementValides.extend(mouvements[0])

        for j in range(len(mouvements[1])):
            if piece.is_enemy_piece(self.board[mouvements[1][j][0]][mouvements[1][j][1]]):
                mouvementValides.append(mouvements[1][j])

        return mouvementValides

    #TODO Vous devez filtrez les mouvements d'un roi
    def filtreRoi(self, piece:Roi) ->list[tuple[int,int]]:
        return []

    #TODO Vous devez filtrez les mouvements d'une reine
    def filtreReine(self, piece:Reine) ->list[tuple[int,int]]:
        return []

    #TODO Vous devez filtrez les mouvements d'un fou
    def filtreFou(self, piece:Fou) ->list[tuple[int,int]]:
        return []

    #TODO Vous devez filtrez les mouvements d'un cavalier
    def filtreCavalier(self, piece:Cavalier) ->list[tuple[int,int]]:
        return []

    #TODO Vous devez filtrez les mouvements d'une tour
    def filtreTour(self, piece:Tour) ->list[tuple[int,int]]:
        return []

    #TODO Trouve le roi et retourne les coordonnees.
    def _find_king(self, equipe) -> Roi:
        return Roi('None')


    #TODO verifie si le joueur est en echec. Il est utilise pour plusieurs methodes
    def is_player_in_check(self, turn:str) -> bool:
        return False

    #TODO verifie si le joueur est en echec et mat
    def is_player_in_check_mate(self, turn:str) -> bool:
        return False

    #TODO verifie si le joueur est en echec et mat et pat
    def is_stale_mate(self, turn:str) ->bool :
        return False

    def setup_stale_mate(self):
        self.board[0][0] = Roi('Noir', (0, 0))
        self.board[1][3] = Roi('Blanc', (1, 3))
        self.board[2][3] = Reine('Blanc', (2, 3))
        self.board[4][4] = Tour('Blanc', (4, 4))

    def setup_standard(self):
        # Place pawns on 2nd row.
        for i, cell in enumerate(self.board[1]):
            self.board[1][i] = Pion('Noir', (1, i))

        # Place pawns on 7th row.
        for i, cell in enumerate(self.board[6]):
            self.board[6][i] = Pion('Blanc', (6, i))

        # Rooks
        self.board[0][0] = Tour('Noir', (0, 0))
        self.board[0][7] = Tour('Noir', (0, 7))
        self.board[7][0] = Tour('Blanc', (7, 0))
        self.board[7][7] = Tour('Blanc', (7, 7))

        # Knights
        self.board[0][1] = Cavalier('Noir', (0, 1))
        self.board[0][6] = Cavalier('Noir', (0, 6))
        self.board[7][1] = Cavalier('Blanc', (7, 1))
        self.board[7][6] = Cavalier('Blanc', (7, 6))

        # Bishops
        self.board[0][2] = Fou('Noir', (0, 2))
        self.board[0][5] = Fou('Noir', (0, 5))
        self.board[7][2] = Fou('Blanc', (7, 2))
        self.board[7][5] = Fou('Blanc', (7, 5))

        # Queens
        self.board[0][3] = Reine('Noir', (0, 3))
        self.board[7][3] = Reine('Blanc', (7, 3))

        # Kings
        self.board[0][4] = Roi('Noir', (0, 4))
        self.board[7][4] = Roi('Blanc', (7, 4))
        