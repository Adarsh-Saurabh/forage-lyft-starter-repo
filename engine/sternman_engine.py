from abc import ABC
from engine import Engine
from car import Car

class SternmanEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage, service_threshold, warning_light_is_on):
        super().__init__(last_service_mileage, current_mileage, service_threshold)
        self.warning_light_is_on = warning_light_is_on

# Instantiate the SternmanEngine
last_service_mileage = 10000
current_mileage = 12000
service_threshold = 2000
warning_light_is_on = True

engine = SternmanEngine(last_service_mileage, current_mileage, service_threshold, warning_light_is_on)
