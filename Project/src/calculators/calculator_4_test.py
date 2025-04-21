from typing import Dict, List
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from .mocks.common_mocks import MockRequest, MockDriverHandler

def test_calculate():
    numbers = [10, 20, 30]
    result = 20
    calculator = 4

    mock_request = MockRequest({ "numbers": numbers })

    driver = MockDriverHandler()
    calculator4 = Calculator4(driver)
    response = calculator4.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response[ "data" ]
    assert "result" in response[ "data" ]

    assert response[ "data" ][ "result" ] == result
    assert response[ "data" ][ "Calculator" ] == calculator

    print()
    print(response)