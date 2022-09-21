#1
'''
sum_of_account=int(input("Enter the sum of money in your account "))
First_share_price=10
second_share_price=15
if (sum_of_account>=50000) and ((sum_of_account%10==0) or (sum_of_account%15==0)):
    print("Rock On!")
else:
    print("Can't Invest")

#2
Programing_grade=int(input("Enter your programing grade between 0-10: "))
Math_grade=int(input("Enter your math grade between 0-10: "))
Teamwork_grade=float(input("Enter your teamwork grade between 0-7.5: "))

if (Programing_grade>=9) and (Math_grade>=9) and (Teamwork_grade>=6):
    print("CLASS_A")
elif (Programing_grade>=8) and (Math_grade>=7) and (Teamwork_grade>5.5):
    print("CLASS_B")
elif (Programing_grade>=6) and (Math_grade + Teamwork_grade>=10.5):
    print("CLASS_C")
elif (Teamwork_grade>Programing_grade) or (Teamwork_grade>Math_grade):
    print("CLASS_D")
else:
     print("Maybe next summer")


#3
Num_1=int(input("Enter a positive number: "))
Num_2=int(input("Enter a second positive number: "))
Action=input("Enter one of these actions: *,/,+,-: ")
if(Action=="*"):
    sum=(Num_1*Num_2)
if(Action=="/"):
    sum=(Num_1/Num_2)
if(Action=="+"):
    sum=(Num_1+Num_2)
if(Action=="-"):
    sum=(Num_1-Num_2)
if (sum>=0):
    print("the result is:")
    print(sum)
else:
    print("Result is not valid")

#4
card_1=int(input("First player: enter the number on your card: "))
card_2=int(input("Second player: enter the number on your card: "))

if (card_1<card_2) and (card_1==1)  :
        print("First player is the winner, first round")
elif (card_1>card_2) and (card_2!=1):
        print("First player is the winner, first round")
elif (card_2<card_1) and (card_2==1):
        print("Second player is the winner, first round")
elif (card_2>card_1) and (card_1!=1):
        print("Second player is the winner, first round")
elif (card_1==card_2):
    print("It's a tie! first round.")
    card_3 = int(input("First player: enter the number on your card: "))
    card_4 = int(input("Second player: enter the number on your card: "))
    if (card_3==card_4):
                print("It's a tie! second round.")
    elif (card_3==1):
                print("First player is the winner, second round")
    elif (card_4==1):
                print("Second player is the winner, second round")
    elif (card_3>card_4) and (card_3-card_4<=2):
                print("First player is the winner, second round")
    elif (card_4>card_3) and (card_4-card_3<=2):
                print("Second player is the winner, second round")
    else:
            print("no winner at this round")


#6
money_in_account=int(input("Enter how much money is in your account: "))
number_of_stocks_to_buy=int(input("Enter the number of stocks you want to buy: "))

pay = ((1.5 + 0.8) * number_of_stocks_to_buy)
pay2=((1.5+0.7)*number_of_stocks_to_buy)
pay3=((1.3 + 0.4) * number_of_stocks_to_buy)
pay4 = ((1.3 + 0.3) * number_of_stocks_to_buy)
pay5 = ((1.1 + 0.1) * number_of_stocks_to_buy)

if (1<=money_in_account<=10000) and (1<=number_of_stocks_to_buy<=500):
    print("You need to pay:",pay)

elif (1<=money_in_account<=10000) and (number_of_stocks_to_buy>500):
        print("You need to pay:",pay2)

elif (10000<=money_in_account<=50000) and (1<=number_of_stocks_to_buy<=250):
    print("You need to pay:", pay3)

elif (10000<=money_in_account<=50000) and (number_of_stocks_to_buy>250):
    print("You need to pay:", pay4)

elif (money_in_account>50000):
    print("You need to pay:", pay5)

'''
#7
name=input("Enter the new employee's name: ")
birthday=int(input("Enter the new employee's birthday in the format (DDMM): "))
DD= birthday // 100
MM= birthday % 100

if (MM==1 or MM==3 or MM==5 or MM==7 or MM==8) and (1<=DD<=31):
    if(DD>=10):
        print(name,"'s birthday is:", DD,"/","0",MM)
    else:
        print(name,"'s birthday is:", "0",DD,"/","0",MM)

elif (MM==2) and (1<=DD<=28):
    if (DD>=10):
        print(name, "'s birthday is:", DD,"/","0",MM)
    else:
        print(name, "'s birthday is:", "0",DD,"/","0",MM)

elif (MM==4 or MM==6 or MM==9 or MM==11) and (1<=DD<=30):
    if (DD>=10):
        print(name, "'s birthday is:", DD,"/","0",MM)
    else:
        print(name, "'s birthday is:", "0", DD, "/", "0", MM)

elif (MM == 10 or MM == 12) and (1 <= DD <= 31):
    if (DD>=10):
        print(name, "'s birthday is:", DD,"/",MM)
    else:
        print(name, "'s birthday is:", "0", DD, "/", "0", MM)
else:
    print("The birthday that you entered is not valid, please try again ")
