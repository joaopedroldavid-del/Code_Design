from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1
from .mocks.common_mocks import MockRequest

def test_calculate():
    number = 30
    calculator = 1
    result = 60.62

    mock_request = MockRequest( body={ "number": number } )
    calculator_1 = Calculator1()

    response = calculator_1.calculate( mock_request )
    
    assert "data" in response
    assert "Calculator" in response[ "data" ]
    assert "result" in response[ "data" ]

    assert response[ "data" ][ "result" ] == result
    assert response[ "data" ][ "Calculator" ] == calculator

    print()
    print(response)

def test_calculate_with_body_error():
    mock_request = MockRequest( body={ "test": 1 } )
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        response = calculator_1.calculate( mock_request )

    assert str(excinfo.value) == "Invalid body"