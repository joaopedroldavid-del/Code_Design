from typing import Dict, List
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from .mocks.common_mocks import MockRequest, MockDriverHandler

def test_calculate():
    numbers = [2, 5, 10]
    calculator = 3
    result = "ERROR: variancia é menor que o valor do elementos multiplicados"
    
    mock_request = MockRequest({ "numbers": numbers })

    driver = MockDriverHandler()
    calculator3 = Calculator3(driver)
    response = calculator3.calculate(mock_request)
    
    assert "data" in response
    assert "Calculator" in response[ "data" ]
    assert "result" in response[ "data" ]

    assert response[ "data" ][ "result" ] == result
    assert response[ "data" ][ "Calculator" ] == calculator

    print()
    print(response)

    


