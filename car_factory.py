from datetime import date
from car import Car
from capulet_engine import CapuletEngine
from spindler_battery import SpindlerBattery
from palindrome_engine import PalindromeEngine
from rorschach_engine import RorschachEngine
from thovex_engine import ThovexEngine

def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    # Instantiate the CapuletEngine
    capulet_engine = CapuletEngine(last_service_mileage, current_mileage, service_threshold)

    # Instantiate the SpindlerBattery
    spindler_battery = SpindlerBattery(last_service_date, current_date, service_threshold)

    # Create a car with the specified engine and battery
    car = Car(engine=capulet_engine, battery=spindler_battery)

    return car

def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    # Instantiate the GlissadeEngine
    glissade_engine = GlissadeEngine(last_service_mileage, current_mileage, service_threshold)

    # Instantiate the SpindlerBattery
    spindler_battery = SpindlerBattery(last_service_date, current_date, service_threshold)

    # Create a car with the specified engine and battery
    car = Car(engine=glissade_engine, battery=spindler_battery)

    return car

def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
    # Instantiate the PalindromeEngine
    palindrome_engine = PalindromeEngine(last_service_date, current_date, warning_light_on)

    # Instantiate the SpindlerBattery
    spindler_battery = SpindlerBattery(last_service_date, current_date, service_threshold)

    # Create a car with the specified engine and battery
    car = Car(engine=palindrome_engine, battery=spindler_battery)

    return car

def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    # Instantiate the RorschachEngine
    rorschach_engine = RorschachEngine(last_service_mileage, current_mileage, service_threshold)

    # Instantiate the SpindlerBattery
    spindler_battery = SpindlerBattery(last_service_date, current_date, service_threshold)

    # Create a car with the specified engine and battery
    car = Car(engine=rorschach_engine, battery=spindler_battery)

    return car

def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    # Instantiate the ThovexEngine
    thovex_engine = ThovexEngine(last_service_mileage, current_mileage, service_threshold)

    # Instantiate the SpindlerBattery
    spindler_battery = SpindlerBattery(last_service_date, current_date, service_threshold)

    # Create a car with the specified engine and battery
    car = Car(engine=thovex_engine, battery=spindler_battery)

    return car
