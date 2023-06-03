import unittest
from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class ServiceableTestCase(unittest.TestCase):
    def test_needs_service(self):
        class MyServiceable(Serviceable):
            def needs_service(self):
                return True

        serviceable = MyServiceable()
        self.assertTrue(serviceable.needs_service())

if __name__ == '__main__':
    unittest.main()
