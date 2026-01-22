# Write a program to Count digits in a number

num=12345
count=0

while num > 0:
    num = num // 10
    count = count + 1
    print("Digits:",count)
    