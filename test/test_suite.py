
import unittest

from test.test_engine.test_capulet_engine import TestCapuletEngine
from test.test_engine.test_sternman_engine import TestSternmanEngine
from test.test_engine.test_willoughby_engine import TestWilloughbyEngine

from test.test_battery.test_spindler_battery import TestSpindlerBattery
from test.test_battery.test_nubbin_battery import TestNubbinBattery

from test.test_tires.test_carrigan_tire import TestCarriganTire
from test.test_tires.test_octoprime_tire import TestOctoprimeTire


# def suite():

#     suite = unittest.TestSuite()
#     suite.addTests([TestCapuletEngine.test_engine_should_be_serviced, TestCapuletEngine.test_engine_should_not_be_serviced,
#                     TestSternmanEngine.test_engine_should_be_serviced, TestSternmanEngine.test_engine_should_not_be_serviced,
#                     TestWilloughbyEngine.test_engine_should_be_serviced, TestWilloughbyEngine.test_engine_should_not_be_serviced])
#     suite.addTests([TestSpindlerBattery.test_battery_should_be_serviced, TestSpindlerBattery.test_battery_should_not_be_serviced, 
#                     TestNubbinBattery.test_battery_should_be_serviced, TestNubbinBattery.test_battery_should_not_be_serviced])
#     suite.addTests([TestCarriganTire.test_tires_should_be_serviced, TestCarriganTire.test_tires_should_not_be_serviced, 
#                     TestOctoprimeTire.test_tires_should_be_serviced, TestOctoprimeTire.test_tires_should_not_be_serviced])
#     return suite


if __name__ == '__main__':
    unittest.main()