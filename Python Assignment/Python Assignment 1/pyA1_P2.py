"""
I was confused that whether,
>> I should print first name after printing last name
or 
>> I should print the the name in reverse. For example
   first name -> Krishna
   last name -> R
   fullname -> Krishna R
   reverse -> R anhsirK

So I did it in both ways
"""


fname = str(input("Enter the firt name: "))
lname = str(input("Enter the last name :"))

print("{} {}".format(lname, fname))
print()

full_name = " ".join([fname, lname])

reverse_name = ""

for i in full_name:
    reverse_name = i+reverse_name

print(reverse_name)

  