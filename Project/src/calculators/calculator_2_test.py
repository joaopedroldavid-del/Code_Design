from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__( self, body: Dict ) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_drivation(self, numbers: List[float]) -> float:
        return 3

def test_calculate():
    numbers = [2.12, 4.62, 1.32]
    calculator = 2
    result = 0.333
    
    mock_request = MockRequest({ "numbers": numbers })

    driver = MockDriverHandler()
    calculator2 = Calculator2(driver)
    response = calculator2.calculate(mock_request)
    
    assert "data" in response
    assert "Calculator" in response[ "data" ]
    assert "result" in response[ "data" ]

    assert response[ "data" ][ "result" ] == result
    assert response[ "data" ][ "Calculator" ] == calculator

    print()
    print(response)

    


