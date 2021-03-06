import unittest
from domain import *

class TestBoard(unittest.TestCase):
    def testPlacePlane(self):
        b=Board('player')
        self.assertEqual(b.getdata(1,1),0)
        with self.assertRaises(DirectionError):
            b.placePlane(5,4,'no direction')
        with self.assertRaises(PlaneError):
            b.placePlane(1,1,'up')
        b.placePlane(5,4,'up')
        self.assertEqual(b.getdata(5,4),-2)
        self.assertEqual(b.getdata(5,3),-1)

    def testMove(self):
        b=Board('player')
        b.placePlane(5,4,'up')
        with self.assertRaises(ValueError):
            b.move(0,9)
        b.move(1, 1)
        self.assertEqual(b.getdata(1, 1), 1)
        with self.assertRaises(ValueError):
            b.move(1,1)
        b.move(5,3)
        self.assertEqual(b.getdata(5,3),-3)
        with self.assertRaises(ValueError):
            b.move(5,3)
        with self.assertRaises(GameWonException):
            b.move(5,4)


class TestPlanes(unittest.TestCase):
    def testPlaneEq(self):
        p=Plane(5,4,'up')
        self.assertEqual(p.getRow(),5)
        self.assertEqual(p.getCol(),4)
        self.assertEqual(p.getDir(),'up')
