Days_stayed=int(input("Enter days of stayed in the hotel"))
Room_type=input("Enter Room type: s/c")
Number_of_guests=int(input("Enter number of guests"))

if (Days_stayed) >= 1 and (Days_stayed) <= 7:
    if (Room_type) == "s" and (Number_of_guests) > 4:
        print("Your number of days is 100")
    elif (Room_type) == "c" and (Number_of_guests) > 6:
        print("Your number of days is 200")
elif (Days_stayed) <=8 and (Days_stayed) <= 14:
    if (Room_type) >= 3 and (Room_type) == "s":
        print("Your number of days is 300")
    elif (Room_type) == "c" and (Number_of_guests) > 5:
        print("your number of days is 400")
elif (Days_stayed) >= 15:
        print("Your number of days is forever")