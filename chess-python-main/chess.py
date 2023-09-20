# --------------------------------------------------------------------------------------------------------
# Chess with PyGame
# Created by Martin Blore 2023
# Full explanation can be found at https://codewithmartin.io/articles/how-to-code-a-chess-game-in-python
# --------------------------------------------------------------------------------------------------------
import sys
import pygame
from board import Board
from images import Images
from pieces.piece import Piece
from pieces.roi import Roi
from pieces.reine import Reine
from pieces.fou import Fou
from pieces.cavalier import Cavalier
from pieces.tour import Tour
from pieces.pion import Pion
from sounds import Sounds

class Chess():
    def __init__(self):
        self.window_size = 1280, 1024
        self.bg_color = 0, 0, 0
        self.board = Board()
        self.images = Images()
        self.sounds = Sounds()
        self.mouse_down = False
        self.font = None
        self.turn = 'Blanc'

        #Ajouter les variables necessaire
        self.check = False
        self.check_mate = False
        self.stale_mate = False

    def init(self):
        pygame.display.init()
        pygame.mixer.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(
            self.window_size, pygame.RESIZABLE)
        pygame.display.set_caption("Chess")

        self.sounds.init()
        self.images.init((self.board.cell_size, self.board.cell_size))
        self.board.setup()

        self.font = pygame.font.SysFont(None, 24)

    #TODO Ici on veut appliquer l'ensemble des regles du jeu
    def apply_rules(self):
        #Regle: On ne peut jouer que si c'est son tour

        #Regle: On ne peut pas finir son tour en etant en echec


        #Regle: Un mouvement = un tour


        #Regle: On regarde si l'autre joueur est en echec pour l'afficher

            #Regle: On regarde si l'autre joueur est en echec et mat

        pass





    #Cette méthode effectue des vérifications
    def update(self):
        # Detect mouse clicks and released.
        if pygame.mouse.get_pressed()[0] == 1:
            if (self.mouse_down is False):
                self.on_mouse_down()
            self.mouse_down = True
        else:
            if (self.mouse_down is True):
                self.on_mouse_up()
            self.mouse_down = False


    #cette méthode est appelé lorsque le bouton gauche de la souris est appuié (so mouse down)
    def on_mouse_down(self):
        mouse_start_click = self.board.board_index_from_mouse_pos()

        if (mouse_start_click[0] != -1):
            # If we clicked on the board with a piece, lets start the drag.
            if (self.board.is_piece_on_square(mouse_start_click[0], mouse_start_click[1])):
                self.board.start_drag(
                    mouse_start_click[0], mouse_start_click[1])

    #cette méthode est appelé lorsque le bouton gauche de la souris est relaché (so mouse up)
    def on_mouse_up(self):
        mouse_end_square = self.board.board_index_from_mouse_pos()

        result = False

        if (mouse_end_square[0] != -1):
            result = self.board.perform_move(mouse_end_square)

        self.board.stop_drag()
        if result == True:
            self.apply_rules()

    def render(self):
        self.screen.fill(self.bg_color)
        self.board.draw(self.screen, self.images)
        text = self.font.render(
            "Tour au Blanc" if self.turn == 'Blanc' else "Tour au Noir", True, (255, 255, 255))
        self.screen.blit(text, (1000, 100))

        if self.check:
            text = self.font.render(
                "Check - White" if self.turn == 'Blanc' else "Check - Black", True, (255, 255, 0))
            self.screen.blit(text, (1000, 150))

        if self.check_mate:
            text = self.font.render(
                "Check Mate - White" if self.turn == 'Blanc' else "Check Mate - Black", True, (255, 0, 0))
            self.screen.blit(text, (1000, 200))

        if self.stale_mate:
            text = self.font.render(
                "Stale Mate - White" if self.turn else "Stale Mate - Black", True, (255, 0, 255))
            self.screen.blit(text, (1000, 250))

        # Draw board labels.
        for row in range(0, 8):
            text = self.font.render(str(8-row), True, (255, 255, 255))
            self.screen.blit(
                text, (80, 100+(row*self.board.cell_size)+(self.board.cell_size/2)-4))
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i, x in enumerate(letters):
            text = self.font.render(str(x), True, (255, 255, 255))
            self.screen.blit(
                text, (100+(i*self.board.cell_size)+(self.board.cell_size/2)-4, 910))

        pygame.display.flip()

    #Ici nous avons l'execution du programme
    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            clock.tick(120)
            self.update()
            self.render()

app = Chess()
app.init()
app.run()
