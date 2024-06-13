
import unittest

from tires.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
        
    def test_tires_should_be_serviced(self):

        tire_wear_state = [0.45, 0.75, 0.5, 0.95]

        tire = CarriganTire(tire_wear_state)
        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_serviced(self):

        tire_wear_state = [0, 0, 0, 0]

        tire = CarriganTire(tire_wear_state)
        self.assertFalse(tire.needs_service())
