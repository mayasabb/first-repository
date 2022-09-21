import os
import util

path = input("Enter the logs file path: ")
#C:\Users\admin\Desktop\maya\week 4\11.9.22\Logs-20220911T072251Z-001\Logs
files_list = os.listdir(path)
os.chdir(path)

event_list = []
event_lists = []


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())


def adding_to_list(file_path):
    with open(file_path, 'r') as f:
        event = f.read()
    return event


for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        read_text_file(file_path)
        event_list.append(adding_to_list(file_path))


new_event_list = []
list_in_list = []

for i in range(len(event_list)):
    list_in_list = event_list[i].splitlines()
    new_event_list.append(list_in_list)
print("events list: ", new_event_list)

valid_list = []
list1 = []

valid_path = r'/week 4/11.9.22/valid data'
f = open(r"/week 4/11.9.22/valid data/valid.txt", "r")
read_valid = f.readlines()

for x in read_valid:
    list1.append(x)
    valid_list.append(list1)
    list1 = []

valid_dct = {}

def change_to_dict(valid_path):  #['Omer', '172.16.13.133', '09:00-20:00']
    for lst in new_valid_list:
        valid_dct[lst[0]] = lst[1], lst[2]


new_valid_list = []
for z in range(len(valid_list)):
    for k in range(len(valid_list[z])):
        list_in = valid_list[z][k].split()
        new_valid_list.append(list_in)

change_to_dict(valid_path)
print(valid_dct)

names = list(valid_dct.keys())
valid_IP_Addresses = []
for i in range(len(valid_dct)):
    valid_IP_Addresses.append(valid_dct[names[i]][0])


valid_hours = []
for i in range(len(valid_dct)):
    valid_hours.append(valid_dct[names[i]][1])


splitted_hour_range = []
for j in range(len(valid_hours)):
    hour_range = valid_hours[j].split("-")
    splitted_hour_range.append(hour_range)


fixed_hour_range = []

for i in range(len(splitted_hour_range)):
    float_hour_range = []
    smallest_hour = float(splitted_hour_range[i][0].replace(':', '.'))
    biggest_hour = float(splitted_hour_range[i][1].replace(':', '.'))
    float_hour_range.append(smallest_hour)
    float_hour_range.append(biggest_hour)
    fixed_hour_range.append(float_hour_range)



logs_hours_list = []
int_hours = []

for i in range(len(new_event_list)):
    log_hour = new_event_list[i][0].split(": ")
    logs_hours_list.append(log_hour)


for j in range(len(logs_hours_list)):
    hour = float(logs_hours_list[j][1].replace(':', '.'))
    int_hours.append(hour)

log_ips_list = []
for i in range(len(new_event_list)):
    log_ip = new_event_list[i][1].split(": ")
    log_ips_list.append(log_ip)



for i in range(len(new_event_list)):
    if new_event_list[i][2] == "Action: Log In":
        for j in range(len(names)):
            if "User: " + names[j] == new_event_list[i][3]:
                if ("IP Address: " + valid_IP_Addresses[j] != new_event_list[i][1]) and (int_hours[j] < fixed_hour_range[j][0] or int_hours[j] > fixed_hour_range[j][1]):
                    line_1 = (names[j], "from", log_ips_list[j][1])
                    line_2 = "Wrong Time and IP Address"
                    util.alert_suspicious(line_1, line_2)
                    break

                elif valid_IP_Addresses[j] != log_ips_list[i][1]:
                    line_1 = (names[j], "from", log_ips_list[j][1])
                    line_2 = "Wrong IP Address"
                    util.alert_suspicious(line_1, line_2)
                    break

                elif int_hours[j] < fixed_hour_range[j][0] or int_hours[j] > fixed_hour_range[j][1]:
                    line_1 = (names[j], "from", log_ips_list[j][1])
                    line_2 = "Wrong Time"
                    util.alert_suspicious(line_1, line_2)
                    break

