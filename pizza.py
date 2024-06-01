size=input("What size of pizza do you want?(S/M/L)")
bill=0
if size=='S' or size=='s':
    bill+=100
    print("Small size pizza price is 100")
elif size=='M' or size=='m':
    bill+=200
    print("Medium size pizza price is 200")
elif size=='L' or size=='l':
    bill+=300
    print("Large size pizza price is 300")
else:
    print("invalid option")
add_pepporinum=input("Do you want to add pepporinum to your pizza?(Y/N)")
if add_pepporinum=='Y' or add_pepporinum=='y':
    if size=='S' or size=='s':
        bill+=30
    else:
        bill+=50
extra_cheese=input("Do you want extra cheese?(Y/N)")
if extra_cheese=='Y' or extra_cheese=='y':
    bill+=20
print(f"Your total bill is {bill}")
