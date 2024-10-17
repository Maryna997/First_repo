from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR

num = Decimal("1.45")
print(num.quantize(Decimal("1.0"), rounding=ROUND_FLOOR))
