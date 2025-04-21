from typing import Dict, List
from flask import Request as FlaskRequest # type: ignore
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError # type: ignore

class Calculator4:

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
            raise HttpUnprocessableEntityError("invalid body")
        
        input_data = list(body["numbers"])
        return input_data

    def __process_data(self, numbers: List[float]) -> float:
        return self.__driver_handler.average(numbers)
        
    def __format_response(self, calc_result: float):
        return {
            "data": {
                "Calculator": 4,
                "result": round(calc_result, 3)
            }
        }