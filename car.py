from engine import Engine
from battery import Battery
from abc import ABC

class Car:
    def __init__(self, engine_last_service_mileage, engine_current_mileage, engine_service_threshold,
                 battery_last_service_date, battery_service_threshold):
        self.__engine = Engine(engine_last_service_mileage, engine_current_mileage, engine_service_threshold)
        self.__battery = Battery(battery_last_service_date, battery_service_threshold)
    
    def needs_service(self):
        if self.__engine.needs_service() or self.__battery.needs_service():
            return True
        else:
            return False
