# Binary to Decimal and Back Converter
# Develop a converter to convert a decimal number to binary
# or a binary number to its decimal equivalent.

def to_decimal(number: str) -> int:
    return int(number, 2)


def to_binary(number: int) -> str:
    return f'{number:b}'
