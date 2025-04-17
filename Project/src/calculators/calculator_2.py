from typing import Dict, List
from flask import Request as FlaskRequest # type: ignore
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json

        input_data = self.__validate_body(body)

        calc_result = self.__process_data(input_data)

        response = self.__format_response(calc_result)

        return response

    def __validate_body(self, body: Dict) -> List:
        if "numbers" not in body:
            raise Exception("Invalid body")
        
        input_data = list(body["numbers"])
        return input_data

    def __process_data(self, numbers: List[float]) -> float:
        first_process = [ (num * 11) ** 0.95 for num in numbers ]

        result = NumpyHandler().standard_drivation(first_process)
        
        return 1/result

    def __format_response(self, calc_result: float) -> Dict:
        return {
             "data": {
                  "Calculator": 2,
                  "result": round(calc_result, 3)
             }
        }
        