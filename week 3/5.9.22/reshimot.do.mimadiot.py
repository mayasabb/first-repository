
'''
#1
def print_num_list(num_list):
    for row in range(len(num_list)):
        for col in range(len(num_list[row])):
            print(num_list[row][col], end= ' ')

        print()

num_list = [[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
print(print_num_list(num_list))


#2
def sum_matrix(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

print(sum_matrix(matrix))


#3
def main_cross(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
              sum += matrix[i][j]
    return sum


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

print(main_cross(matrix))


#4
def print_num_list(num_list):
    for row in range(len(num_list)):
        for col in range(len(num_list[row])):
            print(num_list[row][col], end= ' ')

        print()

def double_list(vip_list, invite_list):
    double_list = []
    double_list.append(vip_list)
    for i in range(len(invite_list)):
        double_list.append(invite_list[i])


    return double_list

invite_list = [["Aviram", "Ohad"] , ["Moti", "Liran", "Roni"]]
vip_list = ["Ofir", "Bar", "Neta"]

new_list = double_list(vip_list, invite_list)

print_num_list(new_list)

vip_not_coming = input("Enter the name of the vip member who can't come: ")
new_list[0].remove(vip_not_coming)

new_friend = input("Enter the name of the new friend who is coming insted: ")
new_list[2].append(new_friend)

print_num_list(new_list)


#5

def print_num_list(num_list):
    for row in range(len(num_list)):
        for col in range(len(num_list[row])):
            print(num_list[row][col], end= ' ')

        print()

mat_size = int(input("Enter size: "))

# matrix of zeroes:
print("==== Zero mat normal ====")
zero_mat_normal = []
row = []
for i in range(mat_size):
    for j in range(mat_size):
        num = i - j
        if num >= 0:
            row.append(num)
        elif num < 0:
            row.append(0)
    zero_mat_normal.append(row)
    row = []

print_num_list(zero_mat_normal)

#6
def list_screens_indexes(tv):
     problem_list = []
     for i in range(len(tv)):
          for j in range(len(tv[i])):
               if tv[i][j] == FAULTY_SCREEN:
                    problem_list.append((i , j))

     return problem_list

WORKING_SCREEN = "work"
FAULTY_SCREEN = "problem"
tv = [[WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
     [WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
     [WORKING_SCREEN, FAULTY_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN],
     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN]]

print(list_screens_indexes(tv))
'''

#7

'''
def tries(board):
    guess = " "
    while guess != "Submarine":
        num_of_guesses = 0
        row = int(input("Enter your row guess: ")) - 1
        col = int(input("Enter your col guess: ")) - 1
        if row >= 0 and row <= 4:
            if col >= 0 and col <= 4:
                guess = board[row][col]

                if guess == "Submarine":
                    print("you guessed right")
                    num_of_guesses += 1
                elif guess == "Empty":
                    print("you guessed wrong")
                    num_of_guesses += 1
                else:
                    print("guess is not valid, try again")

    return ("you guessed", num_of_guesses, "times")
'''

def game(board):
    submarines_guessed = 0
    wrong_guesses = 0
    while submarines_guessed < 3:
        guess = " "
        while guess != "Submarine":
            row = int(input("Enter your row guess: ")) -1
            col = int(input("Enter your col guess: ")) -1
            if row >= 0 and row <=4:
                if col >= 0 and col <= 4:
                    guess = board[row][col]

                    if guess == "Submarine":
                        print("you guessed right")
                        print("you have", wrong_guesses, "missed bombs")
                        submarines_guessed += 1
                    elif guess == "Empty":
                        print("you guessed wrong")
                        wrong_guesses += 1
                        print( "you have", wrong_guesses, "missed bombs")

                    else:
                        print("guess is not valid, try again")

    return ("game ended!")



board = [["Empty", "Empty", "Empty", "Empty", "Empty"],
         ["Empty", "Empty", "Empty", "Empty", "Empty"],
         ["Submarine", "Empty", "Empty", "Empty", "Empty"],
         ["Submarine", "Empty", "Empty", "Empty", "Empty"],
         ["Submarine", "Empty", "Empty", "Empty", "Empty"]]

print(game(board))





