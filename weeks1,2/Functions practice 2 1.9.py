'''
#1
closets_list = []
boxes_list = []

def closets_sizes():
    num_of_closets = int(input("enter the number of closets: "))
    for i in range(num_of_closets):
        closet_length = float(input("Enter the length of your closet: "))
        closet_height = float(input("Enter the height of your closet: "))
        closet_width = float(input("Enter the width of your closet: "))
        closet = (closet_length, closet_height, closet_width)
        closets_list.append(closet)
    return closets_list

def boxes_sizes():
    num_of_boxes = int(input("enter the number of boxes: "))
    for i in range(num_of_boxes):
        box_length = float(input("Enter the length of your box: "))
        box_height = float(input("Enter the height of your box: "))
        box_width = float(input("Enter the width of your box: "))
        box = (box_length, box_height, box_width)
        boxes_list.append(box)
    return boxes_list

def compare_sizes():
    good_box = []
    size = 0
    for closet in closets_list:
        index_min_box = ""
        counter = 0
        min = 100000
        for box in boxes_list:
            if closet[0] <= box[0] and closet[1] <= box[1] and closet[2] <= box[2]:
                size = box[0] * box[1] * box[2]
                if size < min:
                    min = size
                    index_min_box = counter
                    #min_counter = counter
            counter += 1
        if counter == len(boxes_list) and index_min_box == "":
            good_box.append("-1")
        else:
            good_box.append(index_min_box)
            boxes_list[index_min_box] = (0 ,0 ,0)
    return good_box


closets_sizes()
boxes_sizes()
'''


#2
import random

def choosing_words():
    words_list = ["travel", "person", "strong", "street", "turtle", "purple", "orange",
        "potato", "august", "better", "breath", "market", "repair", "school",
        "colony", "online", "carrot", "rabbit", "doctor"]

    word = random.choice(words_list)
    return word

def play(word, right_letters_guessed, wrong_letters_guessed):
    if len(right_letters_guessed) < 6:
        guess = input("hello enter your next guess: ")
        if guess.isalpha() and len(guess) == 1:
            if guess in wrong_letters_guessed or right_letters_guessed:
                print("you already guessed it :(")
            else:
                if guess in word:
                    right_letters_guessed.append(guess)
    return

def right_guess(word, guess, right_letters_guessed):
    print("you guessed right!")
    for i in len(word):
        if word[i] == guess:
            right_letters_guessed.insert(i, guess)

    return right_letters_guessed


right_letters_guessed_1 = []
wrong_letters_guessed_1 = []
right_letters_guessed_2 = []
wrong_letters_guessed_2 = []

player_1 = input("Enter your name: ")
player_2 = input("Enter your name: ")
word1 = choosing_words()
word2 = choosing_words()

while len(right_letters_guessed_1) < 6 or len(right_letters_guessed_2) < 6:
    play(word1, right_letters_guessed_1, wrong_letters_guessed_1)
    play(word2, right_letters_guessed_2, wrong_letters_guessed_2)

if len(right_letters_guessed_1) > len(right_letters_guessed_2):
    print(player_1, "is the winner")

elif len(right_letters_guessed_1) < len(right_letters_guessed_2):
    print(player_2, "is the winner")
