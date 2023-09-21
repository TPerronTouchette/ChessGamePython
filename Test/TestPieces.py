import unittest
from pieces.piece import Piece
from pieces.pion import Pion
from pieces.cavalier import Cavalier
from pieces.fou import Fou
from pieces.roi import Roi
from pieces.reine import Reine
from pieces.tour import Tour

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
        mouvementsExpected = [[(2,3)],[(2,5)],[(3,2)],[(3,6)],[(5,2)],[(5,6)],[(6,3)],[(6,5)]]
        mouvements = self.piece.getMouvement()
        self.assertListEqual(mouvements, mouvementsExpected, "Les mouvements ne correspondent pas à un cavalier")

class TestFou(TestPiece, unittest.TestCase):
    def set_up(self):
        self.piece = Fou("Noir", (4,4))

    def testGetMouvements(self):
        self.set_up()
        mouvementsExpected = [[(3,3), (2, 2), (1, 1), (0, 0)],[(2,5)],[(3,2)],[(3,6)],[(5,2)],[(5,6)],[(6,3)],[(6,5)]]
        mouvements = self.piece.getMouvement()
        for i in mouvements:
            estComplet = True
            j = i[0]

            for k in mouvementsExpected:
                bonneSousListe = True

                if j != k[0]:
                    bonneSousListe = False
                    estComplet = False
        self.assertListEqual(mouvements, mouvementsExpected, "Les mouvements ne correspondent pas à un cavalier")
class TestReine(TestPiece, unittest.TestCase):
    def set_up(self):
        self.piece = Reine("Noir", (4,4))

    def testGetMouvements(self):
        self.set_up()
        mouvementsExpected = [[(2,3)],[(2,5)],[(3,2)],[(3,6)],[(5,2)],[(5,6)],[(6,3)],[(6,5)]]
        mouvements = self.piece.getMouvement()
        self.assertListEqual(mouvements, mouvementsExpected, "Les mouvements ne correspondent pas à un cavalier")
class TestRoi(TestPiece, unittest.TestCase):
    def set_up(self):
        self.piece = Roi("Noir", (4,4))

    def testGetMouvements(self):
        self.set_up()
        mouvementsExpected = [[(2,3)],[(2,5)],[(3,2)],[(3,6)],[(5,2)],[(5,6)],[(6,3)],[(6,5)]]
        mouvements = self.piece.getMouvement()
        self.assertListEqual(mouvements, mouvementsExpected, "Les mouvements ne correspondent pas à un cavalier")
class TestTour(TestPiece, unittest.TestCase):
    def set_up(self):
        self.piece = Tour("Noir", (4,4))

    def testGetMouvements(self):
        self.set_up()
        mouvementsExpected = [[(2,3)],[(2,5)],[(3,2)],[(3,6)],[(5,2)],[(5,6)],[(6,3)],[(6,5)]]
        mouvements = self.piece.getMouvement()

        self.assertListEqual(mouvements, mouvementsExpected, "Les mouvements ne correspondent pas à un cavalier")
if __name__ == '__main__':
    unittest.main()
