# Write a program to Reverse a number

num= 456
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print("Reverse:",rev)