from enum import Enum

class Operator(Enum):
    KYIV = "098"
    LIFE = "063"

Operator.KYIV.value
print(Operator.LIFE.value)

match operator:
    case Operator.KYIV.value:
        pass
    case Operator.LIFE.value:
        pass 
