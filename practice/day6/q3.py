# WAP to count the number of vowels in a string

a="Python Programming Language"
count=0

for i in a: 
    if i in "aeiouAEIOU":
        count+=1

print("Vowels:",count)