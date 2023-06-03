from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, arr):
        self.arr = arr

    def needs_service(self):
        wear_sum = 0
        for i in range(len(self.arr)):
            wear_sum += self.arr[i]
        
        if wear_sum >= 3:
            return True
        else:
            return False