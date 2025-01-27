from .calculator_4 import Calculator4
from pytest import raises
from typing import Dict

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={ "numbers": [4, 6, 8, 10, 12] })
  calculator_4 = Calculator4()

  response = calculator_4.calculate(mock_request)
  print(response)

  assert response == {'data': {'Calculator': 4, 'average': 8.0}}

def test_calculate_with_body_error():
  mock_request = MockRequest(body={ "something": [1, 2, 3, 4, 5] })
  calculator_4 = Calculator4()

  with raises(Exception) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == 'body mal formatado!'
