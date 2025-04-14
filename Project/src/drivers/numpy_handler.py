import numpy
from typing import List

class NumpyHandler:
    def __init__(self) -> None:
        self.__np = numpy
    
    def standard_drivation(self, numbers: list[float]) -> float:
        return self.__np.std(numbers)