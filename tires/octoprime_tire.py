
from tires.tire import Tire

class OctoprimeTire(Tire):

    def __init__(self, tire_wear_state):

        self.tire_wear_state = tire_wear_state

    def needs_service(self):
        
        total = 0
        for t in self.tire_wear_state:
            total += t
        
        if total >= 3:
            return True
        else:
            return False