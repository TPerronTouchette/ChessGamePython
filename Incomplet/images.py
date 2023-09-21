# --------------------------------------------------------------------------------------------------------
# Chess with PyGame
# Created by Martin Blore 2023
# Full explanation can be found at https://codewithmartin.io/articles/how-to-code-a-chess-game-in-python
# --------------------------------------------------------------------------------------------------------
import pygame
import os
from pieces.piece import Piece
from pieces.roi import Roi
from pieces.reine import Reine
from pieces.fou import Fou
from pieces.cavalier import Cavalier
from pieces.tour import Tour
from pieces.pion import Pion

class Images():
    def init(self, size):
        location = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        # Load images keeping them at their base resolution.
        
        self.base_pawn_white = pygame.image.load(os.path.join(location, "images/wp.png")).convert_alpha()
        self.base_pawn_black = pygame.image.load(os.path.join(location, "images/bp.png")).convert_alpha()
        
        self.base_rook_white = pygame.image.load(os.path.join(location, "images/wr.png")).convert_alpha()
        self.base_rook_black = pygame.image.load(os.path.join(location, "images/br.png")).convert_alpha()
        
        self.base_knight_white = pygame.image.load(os.path.join(location, "images/wn.png")).convert_alpha()
        self.base_knight_black = pygame.image.load(os.path.join(location, "images/bn.png")).convert_alpha()

        self.base_bishop_white = pygame.image.load(os.path.join(location, "images/wb.png")).convert_alpha()
        self.base_bishop_black = pygame.image.load(os.path.join(location, "images/bb.png")).convert_alpha()

        self.base_queen_white = pygame.image.load(os.path.join(location, "images/wq.png")).convert_alpha()
        self.base_queen_black = pygame.image.load(os.path.join(location, "images/bq.png")).convert_alpha()

        self.base_king_white = pygame.image.load(os.path.join(location, "images/wk.png")).convert_alpha()
        self.base_king_black = pygame.image.load(os.path.join(location, "images/bk.png")).convert_alpha()

        self.scale(size)

    def scale(self, size):
        # Scale the images from their base resolution to the desired resolution.
        self.pawn_white = pygame.transform.smoothscale(self.base_pawn_white, size)
        self.pawn_black = pygame.transform.smoothscale(self.base_pawn_black, size)

        self.rook_white = pygame.transform.smoothscale(self.base_rook_white, size)
        self.rook_black = pygame.transform.smoothscale(self.base_rook_black, size)

        self.knight_white = pygame.transform.smoothscale(self.base_knight_white, size)
        self.knight_black = pygame.transform.smoothscale(self.base_knight_black, size)

        self.bishop_white = pygame.transform.smoothscale(self.base_bishop_white, size)
        self.bishop_black = pygame.transform.smoothscale(self.base_bishop_black, size)

        self.queen_white = pygame.transform.smoothscale(self.base_queen_white, size)
        self.queen_black = pygame.transform.smoothscale(self.base_queen_black, size)

        self.king_white = pygame.transform.smoothscale(self.base_king_white, size)
        self.king_black = pygame.transform.smoothscale(self.base_king_black, size)

    # Get the image for a piece id.
    def get_image_for_piece(self, piece):

        match(piece.mon_type() + piece.equipe):
            case 'PionBlanc':
                return self.pawn_white
            case 'PionNoir':
                return self.pawn_black
            case 'TourBlanc':
                return self.rook_white
            case 'TourNoir':
                return self.rook_black
            case 'CavalierBlanc':
                return self.knight_white
            case 'CavalierNoir':
                return self.knight_black
            case 'FouBlanc':
                return self.bishop_white
            case 'FouNoir':
                return self.bishop_black
            case 'ReineBlanc':
                return self.queen_white
            case 'ReineNoir':
                return self.queen_black
            case 'RoiBlanc':
                return self.king_white
            case 'RoiNoir':
                return self.king_black
            case _:
                return None
        

