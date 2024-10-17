import decimal
from decimal import Decimal
from decimal import getcontext
from decimal import ROUND_DOWN


print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("0.1") + Decimal("0.2"))


getcontext().prec = 4
print(Decimal("1") / Decimal("7"))
getcontext().prec = 6
print(Decimal("1") / Decimal("7"))
print(Decimal("233") / Decimal("7"))


number = Decimal('3.14159')
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
print(rounded_number)


number = Decimal("1.45")
print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))
print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal('0.000')))