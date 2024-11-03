"""
 Kassi White
 Module 08 LAB - Part B

 This lab is the python program/script
"""
subtotal = 0
num_people = 0


while subtotal == 0:
    try:
        subtotal= float(input("Enter the subtotal for the bill: ")) 

    except ValueError:
        # ValueError, must be numeric
        print("Must be numeric, no other values permitted")
print(f"The subtotal is: ${subtotal:,.2f}")


while num_people < 1:
    try:
        num_people = int(input("Enter the total number of people at the table: "))
        if num_people <= 0: 
            # Since num_people is a divisor in the split_total calculation, it cannot be zero.
            print("Must be greater than zero people at the table")
    except ValueError:
        # ValueError, must be numeric
        print("Must be numeric, and a whole number, no such thing as a fraction of a person.")
print(f"The number of people at the table is: {num_people}.")


tax = subtotal*0.08
total = subtotal + tax
split_total = total/num_people

print(f"The tax for the total bill is: ${tax:,.2f}")
print(f"The total, including tax is: ${total:,.2f}")
print(f"The total cost per person is: ${split_total:,.2f}")