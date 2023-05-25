from abc import ABC
from datetime import datetime
from car import Car
from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date, service_threshold):
        super().__init__(last_service_date, current_date, service_threshold)

# Instantiate the SternmanEngine
last_service_date = last_service_date
current_date = datetime.today()
service_threshold = 2 * 365

battery = SpindlerBattery(last_service_date, current_date, service_threshold)
print(battery)