from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
  def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
    body = request.json
    input_data = self.__validate_body(body)

    calc_result = self.__average(input_data)
    response = self.__format_response(calc_result)

    return response


  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise HttpUnprocessableEntityError("body mal formatado!")
    
    input_data = body["numbers"]
    return input_data
  
  def __average(self, numbers: List[float]) -> float:
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    return average
  
  def __format_response(self, calc_result: float) -> Dict:
    return {
      "data": {
        "Calculator": 4,
        "average": round(calc_result, 2)
      }
    }
