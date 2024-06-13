
import unittest

from tires.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
        
    def test_tires_should_be_serviced(self):

        tire_wear_state = [0.8, 0.8, 0.8, 0.8]

        tire = OctoprimeTire(tire_wear_state)
        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_serviced(self):

        tire_wear_state = [0, 0, 0, 0]

        tire = OctoprimeTire(tire_wear_state)
        self.assertFalse(tire.needs_service())
