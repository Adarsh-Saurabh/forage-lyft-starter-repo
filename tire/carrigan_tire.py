from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, arr):
        self.arr = arr

    def needs_service(self):
        for service in self.arr:
            if service >= 0.9:
                return True
        return False