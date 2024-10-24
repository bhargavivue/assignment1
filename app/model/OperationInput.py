from pydantic import BaseModel

class OperationInput(BaseModel):
    number1: float
    number2: float