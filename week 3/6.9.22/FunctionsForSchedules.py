# building the schedule with days name and free hours:
def building_schedule(hours_per_day ,amount_of_days, schedule, DAY_LIST):
    list = []
    for row in range(hours_per_day + 1):
        for col in range(amount_of_days):
            if row == 0:
                list.append(DAY_LIST[col])
            else:
                list.append("free")
        schedule.append(list)
        list = []

    return schedule

def print_schedule(schedule):
    for row in range(len(schedule)):
        for col in range(len(schedule[row])):
            print(schedule[row][col], end= ' ')

        print()

def user_input():
    inputing = 'go'
    lessons_list = []
    while inputing != 'done':
        name_of_lesson = input("enter the name of the lesson: ")
        lesson_duration = input("enter the lesson duration: ")
        Lesson_day = input("enter the day you want this lesson to be: ")
        lesson_hour = input("enter the hour you want this lesson to begin: ")

        lesson = name_of_lesson + '_' + lesson_duration + '_' + Lesson_day + '_' + lesson_hour

        lessons_list.append(lesson)
        lesson = ' '
        print(" if you want to stop enter done, else enter go")
        inputing = input()

    good_strings_list = []
    good_string = False
    while good_string ==  False:
        for i in range(len(lessons_list)):
            for j in lessons_list[i]:
                if j.isupper() == True:
                    j.lower()
                else:
                    j.lower()
                good_string = True

            good_strings_list.append(lessons_list[i])

    return good_strings_list

def splitting_the_strings(good_string_list):
    splited_strings_list = []
    for i in range(len(good_string_list)):
        new_strings = good_string_list[i].split("_")
        splited_strings_list.append(new_strings)

    return splited_strings_list

def chainging_numbers_into_ints(splited_strings_list):
    for i in range(len(splited_strings_list)):
        for j in range(len(splited_strings_list[i])):
            if j == 1 or j == 3:
                splited_strings_list[i][j] = int(splited_strings_list[i][j])

        return splited_strings_list

def adding_to_sched(schedule, splited_strings_list):
    for i in range(len(splited_strings_list)):
        schedule_hour = (splited_strings_list[i][3] - 7)
        if schedule_hour in schedule:
            if splited_strings_list[i][2] in schedule:
                day_index = schedule.index(splited_strings_list[i][2])
                hours_of_lesson = splited_strings_list[i][1]
                for j in range(hours_of_lesson):
                    if schedule[schedule_hour][day_index] == "free":
                                schedule.insert([schedule_hour][day_index], splited_strings_list[i][0])
                                splited_strings_list.remove(splited_strings_list[i])
                    else:
                        print("this hour is already taken")

    return schedule, splited_strings_list



'''
def adding_lessons_left(splited_strings_list):
    for i in range(len(splited_strings_list)):
        for j in range(len(splited_strings_list[i])):
            if j == 3:














def adding_name_to_schedule(schedule, splited_strings_list):
    temp_index = 0
    for row in range(len(splited_strings_list)):
        for col in range(len(splited_strings_list[row])):
            if col == 2:
                if splited_strings_list[row][col] in schedule:
                    temp_index = schedule.index(splited_strings_list[row][col])
            if col == 3:
                hour = schedule[(splited_strings_list[row][3]) - 7]
                if hour == "free":
                    schedule.insert(hour,splited_strings_list[row][0])
                if hour != "free":
                    print("this hour is already taken by a different lesson")

def adding_name_to_schedule(schedule, splited_strings_list):
    temp_index = 0
    for row in range(len(splited_strings_list)):
        for col in range(len(splited_strings_list[row])):
            if col == 2:
                if splited_strings_list[row][col] in schedule:
                    temp_index = schedule.index(splited_strings_list[row][col])
            if col == 3:
                hour = schedule[(splited_strings_list[row][3]) - 7]
                if hour == "free":
                    schedule.insert(hour,splited_strings_list[row][0])
                if hour != "free":
                    print("this hour is already taken by a different lesson")


def checking_place_in_schedule(splited_strings_list, schedule):
    for row in range(len(splited_strings_list)):
        for col in range(len(splited_strings_list[row])):
            if col == 2:
                if col == 3:
                    if schedule[row][3] == "free":
                        schedule.insert([row][col],splited_strings_list[row][0])
                    elif schedule[row][3] != "free":
                        print("this hour is already taken")
'''





