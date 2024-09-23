medical_reason=input("Is there any Medical reason Y or N:")
attendance=int(input("Enter the Attendance of Students:"))
if medical_reason=="Y":
    print("You are allowed")
else:
    if attendance>=75:
        print("You are allowed")
    else:
       print("You are not allowed")
 
