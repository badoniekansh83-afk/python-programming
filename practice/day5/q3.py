# Write a program to check whether the given number is perfect number or not

num=6
sum=0
for i in range(1,num):
    if num % i==0:
        sum += i
if sum == num:
    print("Perfect Number")
else:
    print("Not a perfect number")