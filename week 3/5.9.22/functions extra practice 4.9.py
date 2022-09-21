'''
#1
def multiplaylist (tuple):
    for i in range(len(tuple)):
        number_of_values = len(tuple)
        summing = sum(tuple)
        avr = summing ** (1/number_of_values)

    return avr

tuple = (1, 2, 3)
print(multiplaylist(tuple))

#2
def three_max():
    max_value = 0
    sum = list[0] * list[1] * list[2]
    sum_add = list[0] * list[1] + list[2]

    if sum >= sum_add:
        max_value = sum
    elif sum_add >= sum:
        max_value = sum_add

    return max_value

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))
list = [num1, num2, num3]

print(three_max())

'''

#3

def changing_names(students_list, new_students_list):
    for i in range(len(new_students_list)):
        reformat = input("Is the first letter of the name", i, "capital? Enter True\ False")
        if reformat = True:
            new_students_list[i].title()


students_input = input("Enter students full names with space: ")
students_list = students_input.split()
new_students_input = input("Enter new students full names with space: ")
new_students_list = new_students_input.split()


