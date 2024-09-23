units=int(input("Enter The Numbers Consumed:"))
#if units are under 50
if(units < 50):
    amount = units * 2.60
    surcharge = 25

# if units are less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

#if units are less than or equal to 200
elif(units <= 200):
    amount = 130 +162.50 + ((units-100) * 5.26)
    surcharge = 45

 #check for all the cases other than mentioned
 #when units consumed are more than 200
else:
     amount = 130 + 526 + 162.50 + ((units - 200) * 8.45)
     surcharge = 75

total= amount+surcharge
print("Electricity bill:", total)

   


       