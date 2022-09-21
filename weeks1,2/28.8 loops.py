'''
#5
num=0
sum=0

while sum<=100:
    print(sum)
    num+=1
    sum+=num

import random

#1
number_of_players=int(input("Enter the number of players: "))


for i in range(1,number_of_players+1):
    num=random.randint(0,10)
    print("player",i, "please type your guess: ")
    guess=int(input())

    if num == guess:
        print("win")
        print("you guessed 1 time.")
    else:
        num_of_guess=1
        while num!=guess:
            if guess<num:
                num_of_guess += 1
                print("too low. try again")
                guess=int(input("player please type your next guess: "))
            elif guess>num:
                num_of_guess += 1
                print("too high. try again")
                guess=int(input("player please type your next guess: "))

        print("win")
        print("you guessed",num_of_guess, "times.")

#2
num=int(input("Enter a number: "))

for i in range (1,num+1):
    for j in range (1,num+1):
        print(i*j, end=" ")
    print("\n")


#2
num=int(input("Enter a positive number: "))
solution_str=""
while num!= -1:
    for i in range (1,num+1):
        solution_str=""
        for j in range (1,num+1):
            solution = i * j
            solution_str+= (str(solution)+"\t")
        print(solution_str)

    print("if you want to stop enter -1: ")
    num = int(input("Enter a positive number: "))
    if num== -1:
        break


#שאלת בונוס למתקדמים

num=int(input("Enter a number: "))
for i in range(1,num+1):
     if i%7==0:
         print("boom")
     elif i%10==7:
         print("boom")
     else:
        print(i)

#שאלת בונוס למתקדמות: חלק ב'
num= int(input("Enter a number between 1-9: "))
num2= int(input("Enter a number to stop in: "))
for i in range(1,num2+1):
     if i%num==0:
         print("boom")
     elif i%10==num:
         print("boom")
     else:
        print(i)


#שאלות ניצנים למתקדמים:
#2
sum_length=0

for i in range(1,5):
    print("Enter the name of road",i ,":")
    name= input()
    print("Enter the length of road",i, ": ")
    length=float(input())

    if length>15:
        print(name)
    sum_length+=length

print("the sum length of israel road is: ",sum_length)


#4
num_big_orders=0
for i in range(1,6):

    print("Enter costumer number",i,"'s" " name: ")
    name= input()

    print("Enter number of boxes costumer number",i,"orderd: ")
    num_of_boxes=int(input())

    price= 25 * num_of_boxes

    if num_of_boxes < 3:
        sum_price= price + 20
    else:
        sum_price= price

    if num_of_boxes>20:
        num_big_orders+=1

    print(name, "needs to pay", sum_price)
print("There are", num_big_orders, "big orders.")


#6
times=0
for i in range(1,10):
    num=str(i)
    times+=1
    print(num*times)
 '''
import random

#8
num= random.randint(1,100)
for i in range(1,6):
    while num%10==0:
        print((str(num)) * 10)

