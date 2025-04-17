from typing import Dict, List
from flask import Request as FlaskRequest # type: ignore
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        first_process_result = self.__first_process(input_data)
        calc_result = self.__second_process(first_process_result)

        response = self.__format_response(1/calc_result)

        return response

    def __validate_body(self, body: Dict) -> List:
        if "numbers" not in body:
            raise Exception("Invalid body")
        
        input_data = list(body["numbers"])
        return input_data

    def __first_process(self, numbers: List[float]) -> List[float]:
        result = []

        for number in numbers:
            processed = (number * 11) ** 0.95
            result.append(processed)

        return result
        
    def __second_process(self, numbers: List[float]) -> float:
            return NumpyHandler().standard_drivation(numbers)

    def __format_response(self, calc_result: float) -> Dict:
        return {
             "data": {
                  "Calculator": 2,
                  "result": round(calc_result, 3)
             }
        }
        