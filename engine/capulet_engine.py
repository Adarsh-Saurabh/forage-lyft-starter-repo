from abc import ABC
from engine import Engine
from car import Car

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage, service_threshold):
        super().__init__(last_service_mileage, current_mileage, service_threshold)

# Specify the values for last_service_mileage, current_mileage, and service_threshold
last_service_mileage = 25000
current_mileage = 28000
service_threshold = 30000

# Instantiate the SternmanEngine class with the specified values
engine = SternmanEngine(last_service_mileage, current_mileage, service_threshold)
