# Given the code below, insert the correct method to convert all uppercase letters to lowercase and all lowercase letters to uppercase.



my_string = "In 2010, someone paid 10k Bitcoin for two pizzas."
string2=[]
for i in my_string:
    if i.isupper():
        string2.append(i.lower())
    else:
        string2.append(i.upper())
string3=''.join(string2)
print(string3)

#Easiest way

print(my_string.swapcase())