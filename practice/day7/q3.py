# WAP to Convert a binary number to decimal without using built-in functions.

binary = 1011
decimal = 0
p = 0

while binary > 0:
    d = binary % 10
    decimal += d * (2 ** p)
    p += 1
    binary //= 10

print("Decimal:", decimal)