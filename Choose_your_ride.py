print("Choose your Ride:")
print("1. Bike")
print("2. Car")
#input choose 1 or 2
#select your ride
choice= int(input("Enter your choice:"))

#user enters 1
if (choice==1):
    print("What type of bike?")
    print("1. scooty\n")
    print("2. motorcycle\n")

#conditioning for selecting the bike type
    choice2=int(input("your Bike type:"))
    if choice2==1:
        print("you have selected scooty")
    else:
        print("you have choosen motorcycle")

#option2
elif (choice==2):
    print("What type of car?")
    print("1.sedan")
    print("2.SUV")
    choice3=int(input("whats ur choice:"))
    if choice3==1:
        print("your Sedan is On its way")
    elif choice==2:
        print("Your SUV is on its way")
    
else:
    print("you have a wrong choice")
