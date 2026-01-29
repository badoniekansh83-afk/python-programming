# WAP to check for the LCM of two number

a=12
b=18
x,y=a,b

while y!=0:
    x,y=y,x%y

gcd=x
lcm=(a*b) // gcd
print("LCM: ",lcm)