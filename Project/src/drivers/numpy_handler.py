import numpy # type: ignore
from typing import List
from .interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy
    
    def standard_drivation(self, numbers: list[float]) -> float:
        return self.__np.std(numbers)
    
    def variance(self, numbers: list[float]) -> float:
        return self.__np.var(numbers)