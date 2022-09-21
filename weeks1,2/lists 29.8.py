'''
#1
my_list=[3,"hello",-68,'x',100]
index=int(input("enter a number between 0-4: "))
if index>=0 and index<=4:
    print(my_list[index])
else:
    print("Error")

#2
my_list=[3,7,-68,55,100]
num=int(input("enter a number: "))

if (num in my_list)==True:
    print("the index of this number is:", my_list.index(num))
else:
    print("This number is not in the list. :(")


#3
my_list=[]
num=input("enter value, if you want to stop and print the list, enter stop: ")
while num != "stop":
    my_list.append(num)
    num=input("enter value, if you want to stop and print the list, enter stop: ")
print(my_list)

#4
my_list=["orenge","banana","apple","kiwi"]
index=int(input("Enter index between 0-3: "))
if index>=0 and index<=3:
    my_list.insert(index,"pineapple")
    print(my_list)
else:
    print("The index you entered is not valid")

#5
my_list=[15,4,21,3,7,11]
player=int(input("Enter the number of the player who left: "))

if (player in my_list) == True:
    my_list.remove(player)
    print(my_list)
else:
    print("this player is already not in the grope")


#6
my_list=[2,4,76,198]
index=int(input("Enter an index between 0-3: "))

if index>=0 and index<=3:
    my_list.pop(index)
    print(my_list)
else:
    print("The index you entered is not valid")


#7
list1=[1,2,3,4]
list2=[6,7,8,9,10]

print("In list number 1 there are",len(list1),"values")
print("In list number 2 there are",len(list2),"values")

#8
my_list=["o", "hat", "aba", "1221", "umbrella", "pickup","22.3.22"]
print(my_list[2],my_list[3],my_list[5],my_list[6])


#9
int_list=[1,2,6,0,-9,50]
floats_list=[0.5,-9.3,40.7,8.1]

print(int_list+floats_list)



#10
my_list = [7, -40.3, "hello", 222, '+']

for i in range(len(my_list)):
    print(type(my_list[i]))


#11
list=[3,5,45,97,32,22,10,19,39,43]
newlist=[x for x in list if x % 2== 0]
print(newlist)


import random

list_1 = [1, 2, 3, 4, 5]
newlist = []
indexlist = []

while len(newlist) != len(list_1):
    index = random.randint(0, len(list_1)-1)

    if index not in indexlist:
        indexlist.append(index)
        newlist.append(list_1[index])

print(newlist)



print(newlist)


#13
first_list = ["father", "kayak", "madam", "Ronaldo", "Noa", "David"]

second_list = ["xavi", "Xman", "banana", "aoN", "madam", "kayak"]

finel_list = []

for i in range(len(second_list)):
    second_list[i] = second_list[i][::-1]

for i in range(len(first_list)):
    if first_list[i] in finel_list:
        finel_list.remove(first_list[i])
    finel_list.append(first_list[i])

    if second_list[i] in finel_list:
        finel_list.remove(second_list[i])
    finel_list.append(second_list[i])

print(finel_list)
'''

#14

grades_list = []

for i in range(1,6):
    print("Enter grade ", i, ": ")
    grade= int(input())
    grades_list.append(grade)


print(grades_list)
sum=grades_list[0] + grades_list[1] + grades_list [2] + grades_list[3] + grades_list[4]

average_grade = sum/len(grades_list)
print("your class average grade is: " ,average_grade)

new_grade_list=[]

for j in range(1,6):

    if grades_list[j] >= 80:
        new_grade_list=[j] = grades_list[j] + 10

    elif grades_list[j] >= 60 and grades_list[j] <= 80:
        new_grade_list=[j] = grades_list[j] + 7

    elif grades_list[j] < 60:
        new_grade_list=[j] = grades_list[j] + 5

new_grade_list.sort()
print(new_grade_list)

sum2= new_grade_list[0] + new_grade_list[1] + new_grade_list[2] + new_grade_list[3] + new_grade_list[4]

new_average_grade = sum2/len(new_grade_list)
print("your class new average grade is: " ,new_average_grade)









