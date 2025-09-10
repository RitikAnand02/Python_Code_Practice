# Nested if else() statement in the python

x=int(input("Enter the Value:: "))
if(x>50 and x<100):
    if(x%2==0):
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Your Value is not in Range")