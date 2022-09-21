import FunctionsForSchedules

STARTING_HOUR = 8
DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

amount_of_days = int(input("Enter the amount of days:"))
hours_per_day = int(input("Enter the hours per days:"))
schedule = []

# Initializing the schedule
# TODO

FunctionsForSchedules.building_schedule(hours_per_day, amount_of_days, schedule, DAY_LIST)
FunctionsForSchedules.print_schedule(schedule)

good_string_list = FunctionsForSchedules.user_input()
print(good_string_list)

splited_strings_list = FunctionsForSchedules.splitting_the_strings(good_string_list)
print(splited_strings_list)

splited_strings_list= FunctionsForSchedules.chainging_numbers_into_ints(splited_strings_list)

int_nums = FunctionsForSchedules.chainging_numbers_into_ints(splited_strings_list)
print(int_nums)

adding_lessons_to_schedule = FunctionsForSchedules.adding_to_sched(schedule, splited_strings_list)
print(adding_lessons_to_schedule)













'''
# The data is inserted:
# [name of class]_[how many hours the class]_[day]_[starting hour]
# TODO

# Initial insertion of lessons
# TODO

# Final insertion of lessons
# TODO


for day in range(amount_of_days):
    print(DAY_LIST[day] + ": " + str(schedule[day]))
'''