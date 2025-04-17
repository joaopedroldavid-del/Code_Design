from typing import Dict
from .calculator_2 import Calculator2

class MockRequest:
    def __init__( self, body: Dict ) -> None:
        self.json = body

def test_calculate():
    numbers = [2.12, 4.62, 1.32]
    calculator = 2
    result = 0
    
    mock_request = MockRequest({ "numbers": numbers })

    calculator2 = Calculator2()
    response = calculator2.calculate(mock_request)
    
    assert "data" in response
    assert "Calculator" in response[ "data" ]
    assert "result" in response[ "data" ]

    #assert response[ "data" ][ "result" ] == result
    assert response[ "data" ][ "Calculator" ] == calculator

    print()
    print(response)

    


