from car import Car
from abc import ABC
from datetime import datetime

class Battery(Car, ABC):
    def __init__(self, last_service_date, current_date, service_threshold):
        self.__last_service_date = last_service_date
        self.__current_date = datetime.today()
        
    
    def needs_service(self):
        if self.__current_date - self.__last_service_date >= self.__service_threshold :
            return True
        else:
            return False
    