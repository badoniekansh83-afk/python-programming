# Write a program to check whether a prime number or not

num=7
b=0

for i in range(2,num):
    if num % i == 0:
        b=1
if b == 0:
    print("Prime Number")
else:
    print("Not Prime Number")
    