from tires.tire import Tire

class CarriganTire(Tire):

    def __init__(self, tire_wear_state):

        self.tire_wear_state = tire_wear_state

    def needs_service(self):
        
        for t in self.tire_wear_state:
            if t >= 0.9:
                return True
        return False