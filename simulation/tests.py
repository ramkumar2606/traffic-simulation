"""
Unit test cases
"""
import unittest
from .simulation import Simulation


class TrafficLightSimulationTest(unittest.TestCase):
    """
    Unit test cases
    """
    def test_run_positive(self):
        """
        Testcase in positive scenario
        """
        simulation = Simulation()
        simulation.red_seconds = 5
        simulation.yellow_seconds = 5
        simulation.red_seconds = 5

        simulation.run()
        simulation.stop()  # ToDO: Asynchrously call this method to interrupt the process
        self.assertTrue(True, "Simulation successful")  # If we reached here without exceptions, that means successful

    def test_validate_seconds(self):
        """
        Testcase for validate method
        """
        simulation = Simulation()
        op = simulation.validate_seconds(-1)
        assert op==False


if __name__ == '__main__':
    unittest.main()

