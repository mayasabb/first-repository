#הכנסת מס משתתפים
import random

num_of_players = int(input("Rony's mom, enter the number of the players: "))
chair_line=[]
Music_on= bool
left_line=[]

for i in range(1, num_of_players+1):
    print("Enter the name of player", i, ": ")
    name =(input())
    chair_line.append(name)

standing = random.choice(chair_line)
chair_line.remove(standing)

print(standing, "is standing")

print("Rony's mom, turn on music")
Music_on = input("Is the music on? answer True or False: ")
while num_of_players >= 1:
    if Music_on == 'True':
        chair_line.append(standing)
        standing = random.choice(chair_line)
        chair_line.remove(standing)
        Music_on = input("Is the music still on? answer True or False: ")

    elif Music_on == 'False':
        print("The player who left the game is: ", standing)
        chair_line.append(standing)
        chair_line.remove(standing)
        new_chair_line = chair_line
        print("the new chair list is: ", random.shuffle(chair_line))
        print(new_chair_line)
        num_of_players = len(new_chair_line)

        if num_of_players == 1:
             print("The winner is",new_chair_line[0])
             break

        else:
            print("keep playing!")
