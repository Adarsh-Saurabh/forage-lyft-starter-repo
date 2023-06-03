import unittest
from engine import Engine
from sternman_engine import SternmanEngine
from datetime import datetime
from willoughby_engine import WilloughbyEngine
from capulet_engine import CapuletEngine

class EngineTest(unittest.TestCase):

    def test_needs_service_sertnman(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        self.assertTrue(engine.needs_service())


    def test_needs_service_willoughby(self):
        current_mileage = 50000
        last_service_mileage = 10000

        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        engine2 = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        self.assertFalse(engine.needs_service())
    
    def test_needs_service_capulet(self):
        current_mileage = 50000
        last_service_mileage = 10000

        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        self.assertTrue(engine.needs_service())


if __name__ == '__main__':
    unittest.main()



# import unittest
# from engine import Engine
# from sternman_engine import SternmanEngine
# from datetime import datetime
# from willoughby_engine import WilloughbyEngine

# class EngineTest(unittest.TestCase):
#     def test_needs_service_sternman(self):
#         warning_light_is_on = True
#         engine = SternmanEngine(warning_light_is_on)
#         self.assertTrue(engine.needs_service())

#     def test_needs_service_willoughby(self):
#         current_mileage = 500000
#         last_service_mileage = 10000
#         engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
#         self.assertTrue(engine.needs_service())

# if __name__ == '__main__':
#     unittest.main()
