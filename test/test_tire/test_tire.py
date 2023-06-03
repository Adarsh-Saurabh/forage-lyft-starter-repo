import unittest
from datetime import datetime
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestTire(unittest.TestCase):
    
    def test_octoprime(self):
        a = 0.9
        b = 0.9
        c = 0.9
        d = 0.9
        arr = [a, b, c, d]
        tire = OctoprimeTire(arr)
        self.assertTrue(tire.needs_service())


    def test_carrigan(self):
        a = 0.2
        b = 0.3
        c = 0.9
        d = 0.8
        arr = [a, b, c, d]
        tire = CarriganTire(arr)
        self.assertTrue(tire.needs_service())


if __name__ == '__main__':
    unittest.main()


