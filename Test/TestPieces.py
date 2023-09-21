import unittest
from pieces.piece import Piece
from pieces.pion import Pion
from pieces.cavalier import Cavalier

class TestPiece(unittest.TestCase):
    #__test__ = False
    def set_up(self):
        self.piece = Piece()

    def testTypeGetMouvements(self):
        #piece = Pion("Noir", (1, 0))
        self.set_up()
        mouvements = self.piece.getMouvement()
        self.assertTrue(isinstance(mouvements, list), "getMouvement() ne retourne pas une liste ")
        self.assertTrue(isinstance(mouvements[0], list), "getMouvement() ne retourne pas une liste de liste")
        self.assertTrue(isinstance(mouvements[0][0], tuple),
                        "getMouvement() ne retourne pas une liste de liste de tuple")
        self.assertTrue(isinstance(mouvements[0][0][0], int),
                        "getMouvement() ne retourne pas une liste de liste de tuple de 2 int")
        self.assertTrue(isinstance(mouvements[0][0][1], int),
                        "getMouvement() ne retourne pas une liste de liste de tuple de 2 int")
        self.assertEqual(len(mouvements[0][0]), 2,
                         "getMouvement() ne retourne pas une liste de liste de tuple de 2 int")


class TestPion(TestPiece, unittest.TestCase):
    #__test__ = True
    def set_up(self):
        self.piece = Pion("Noir", (1,0))

    """
    def testTypeGetMouvement(self):
        piece = Pion("Noir", (1, 0))
        mouvements = piece.getMouvement()
        self.assertTrue(isinstance(mouvements, list), "getMouvement() ne retourne pas une liste ")
        self.assertTrue(isinstance(mouvements[0], list), "getMouvement() ne retourne pas une liste de liste")
        self.assertTrue(isinstance(mouvements[0][0], tuple), "getMouvement() ne retourne pas une liste de liste de tuple")
        self.assertTrue(isinstance(mouvements[0][0][0], int), "getMouvement() ne retourne pas une liste de liste de tuple de 2 int")
        self.assertTrue(isinstance(mouvements[0][0][1], int), "getMouvement() ne retourne pas une liste de liste de tuple de 2 int")
        self.assertEqual(len(mouvements[0][0]), 2, "getMouvement() ne retourne pas une liste de liste de tuple de 2 int")
    """
    def testGetMouvementsNoir(self):
        piece = Pion("Noir", (1, 0))
        mouvements = piece.getMouvement()
        self.assertListEqual(mouvements, [[(2,0), (3,0)], [(2, 1), (2, -1)]])

    def testGetMouvementsBlanc(self):
        piece = Pion("Noir", (6, 0))
        mouvements = piece.getMouvement()
        self.assertListEqual(mouvements, [[(5,0), (4,0)], [(5, 1), (5, -1)]])

class TestCavalier(TestPiece, unittest.TestCase):
    def set_up(self):
        self.piece = Cavalier("Noir", (4,4))

    def testGetMouvements(self):
        self.set_up()


if __name__ == '__main__':
    unittest.main()
