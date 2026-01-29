# WAP to check for the GCD of two number

a=12
b=18

while b!=0:
    a,b=b,a%b
print("GCD:",a)