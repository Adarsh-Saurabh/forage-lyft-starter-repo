from car import Car
from abc import ABC

class Engine(Car, ABC):
    def __init__(self, last_service_mileage, current_mileage, service_threshold):
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage
        self.__service_threshold = service_threshold
    
    def needs_service(self):
        if self.__current_mileage - self.__last_service_mileage >= self.__service_threshold or self.warning_light_is_on:
            return True
        else:
            return False
    