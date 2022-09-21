print("Every player takes a card")
Harry_card=int(input("Enter the number on your card"))
Harmaiony_card=int(input("Enter the number on your card"))
Ron_card=int(input("Enter the number on your card"))

if (Harry_card > Harmaiony_card+ Ron_card):
    print("Harry is the winner!")

elif (Harmaiony_card > Harry_card+ Ron_card):
    print("Harmaiony is the winner!")

elif (Ron_card > Harry_card + Harmaiony_card):
    print("Ron is the winner")
