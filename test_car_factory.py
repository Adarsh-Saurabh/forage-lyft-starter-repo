import unittest
from car_factory import CarFactory

class CarFactoryTests(unittest.TestCase):

    def test_create_calliope(self):
        current_date = '2023-05-25'
        last_service_date = '2003-03-10'
        current_mileage = 5000
        last_service_mileage = 4000

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)

        self.assertEqual(car.engine.__class__.__name__, 'CapuletEngine')
        self.assertEqual(car.battery.__class__.__name__, 'SpindlerBattery')

    def test_create_glissade(self):
        current_date = '2023-05-25'
        last_service_date = '2023-03-10'
        current_mileage = 5000
        last_service_mileage = 4000

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)

        self.assertEqual(car.engine.__class__.__name__, 'WilloughbyEngine')
        self.assertEqual(car.battery.__class__.__name__, 'SpindlerBattery')

    def test_create_palindrome(self):
        current_date = '2023-05-25'
        last_service_date = '2023-03-10'
        warning_light_is_on = True

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)

        self.assertEqual(car.engine.__class__.__name__, 'SternmanEngine')
        self.assertEqual(car.battery.__class__.__name__, 'SpindlerBattery')

    def test_create_rorschach(self):
        current_date = '2023-05-25'
        last_service_date = '2023-03-10'
        current_mileage = 5000
        last_service_mileage = 4000

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)

        self.assertEqual(car.engine.__class__.__name__, 'WilloughbyEngine')
        self.assertEqual(car.battery.__class__.__name__, 'NubbinBattery')

    def test_create_thovex(self):
        current_date = '2023-05-25'
        last_service_date = '2023-03-10'
        current_mileage = 5000
        last_service_mileage = 4000

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)

        self.assertEqual(car.engine.__class__.__name__, 'CapuletEngine')
        self.assertEqual(car.battery.__class__.__name__, 'NubbinBattery')

if __name__ == '__main__':
    unittest.main()
