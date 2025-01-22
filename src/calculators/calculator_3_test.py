from src.calculators.calculator_3 import Calculator3
from pytest import raises
from typing import Dict, List

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler:
  def variance(self, numbers: List[float]) -> float:
    return 1

def test_calculate_with_variance_error():
  mock_request = MockRequest({ "numbers": [0, 1, 2, 2, 3] })
  calculator_3 = Calculator3(MockDriverHandler())

  with raises(Exception) as excinfo:
    calculator_3.calculate(mock_request)

  assert str(excinfo.value) == 'Falha no processo: Variância maior que multiplicação.'

def test_calculate():
  mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })

  calculator_3 = Calculator3(MockDriverHandler())

  response = calculator_3.calculate(mock_request)
  assert response == {'data': {'Calculator': 3, 'value': 1, 'success': True}}
