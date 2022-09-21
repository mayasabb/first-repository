'''
numbers = [14, 4, 1]

def list_sum(numbers):
    return sum(numbers)

list_sum(numbers)
print(list_sum(numbers))


#2
numbers = [1, 1, 2, 2, 3, 3]
print ("The list is: " + str(numbers))
result = []

def list_remove():
   for i in numbers:
        if i not in result:
            result.append(i)

list_remove()
print ("The list after removing duplicates : " , result)


#3

def find_max_substring(word, word_list):
    max_len = 0
    for this_word in word_list:
        temp_index = 0
        counter = 0
        for i in range(len(this_word)):
            for j in range(temp_index, len(word)):
                if this_word[i] == word[j]:
                    temp_index = j
                    counter += 1
                    break
        if counter == len(this_word):
            if counter > max_len:
                max_len = counter
    return max_len


word = "computer"
word_list = ["com", "pmo", "cpter", "cpmuter"]
max_len = find_max_substring(word, word_list)
print("the length of the longest substring is : ", max_len)


#4
# advanced
import random

YES = "y"
NO = "n"

game_list = []
number_of_participants = int(input("Enter the number of participants: "))

def adding_players():
    participant = input("Enter participant's name: ")
    game_list.append(participant)

for i in range(number_of_participants):
    adding_players()
print("Let the game begin!")
print(game_list)

def playing():
    standing_participant = game_list.pop()
    is_music = input("Is the music still playing? y/n")
    while is_music != YES and is_music != NO:
        is_music = input("Please enter valid input y/n")

    while is_music == YES:
        random_index = random.randint(0, len(game_list) - 1)
        temp_var = game_list[random_index]
        game_list[random_index] = standing_participant
        standing_participant = temp_var
        is_music = input("Is the music still playing? y/n")
        while is_music != YES and is_music != NO:
            is_music = input("Please enter valid input y/n")
    print(str(standing_participant) + " is out")
    print(game_list)

while len(game_list) > 1:
    playing()
print("The winner is:" + str(game_list[0]))

'''

