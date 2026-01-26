# write a program to find a number whether a palindrome or not

num=121
temp=num 
rev=0

while num>0:
    rev=rev*10 + num%10
    num //=10
if temp == rev:
    print("It is palindrome")
else:
    print("It is not palindrome")