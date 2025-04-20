from typing import Dict, List
from flask import Request as FlaskRequest # type: ignore
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

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

    def __process_data(self, numbers: List[float]) -> str:
        
        first_process = 1
        for num in numbers:
            first_process *= num

        second_process = self.__driver_handler.variance(numbers)
        
        if first_process > second_process:
            return "Sucesso"

        return "ERROR: variancia é menor que o valor do elementos multiplicados"

    def __format_response(self, calc_result: str) -> Dict:
        return {
             "data": {
                  "Calculator": 3,
                  "result": calc_result
             }
        }
        