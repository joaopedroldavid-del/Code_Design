from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__( self, body: Dict ) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_drivation(self, numbers: List[float]) -> float:
        return 3
    def variance(self, numbers: List[float]) -> float:
        return 100
    def average(self, numbers: List[float]) -> float:
        return 20