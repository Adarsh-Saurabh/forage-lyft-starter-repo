import unittest
from datetime import datetime
from nubbin_battery import NubbinBattery
from spindler_battery import SpindlerBattery

class TestBattery(unittest.TestCase):
    
    def test_nubbin(self):
        current_date = datetime.today()
        last_service_date = datetime(2022, 12, 11)

        battery = NubbinBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_spindler(self):
        current_date = datetime.today()
        last_service_date = datetime(2022, 12, 11)

        battery = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
