# write a program to find the sum of the digit of a number

num=123
sum=0
while num>0:
    sum+=num%10
    num //=10
print("sum: ",sum)