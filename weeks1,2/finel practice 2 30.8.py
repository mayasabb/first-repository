
name_ID_dict = {"1":"Dan",
                "2":"Shir",
                "3":"Rotem",
                 "4":"May",
                 "5":"noam",
                 "6": "Matan"}

name_grade_dict = {}

for i in range(len(name_ID_dict)):
    grade = int(input("enter student grade: "))
    id = (input("enter student id: "))

    if id in name_ID_dict:
        name_grade_dict.update({name_ID_dict[id]: grade})

print(name_grade_dict)


new_dict = {"1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": []}

ids = new_dict.keys()
print(ids)

first_ids = name_ID_dict.keys()
print(first_ids)

for i in range(len(new_dict)):
    if ids == first_ids :
        new_dict[i][0] = name_ID_dict[i]
        new_dict[i][1] = name_grade_dict[i]

print(new_dict)



'''
keys_list = new_dict.keys()
keys_list_name_ID_dict = name_ID_dict.keys()
keys_list_name_grade_dict = name_grade_dict.keys()

for i in range(len(new_dict)):
    if keys_list[i] == keys_list_name_ID_dict[i]:
        new_dict[i].append(keys_list_name_grade_dict[i])
        new_dict[i].append(name_grade_dict[i])
print(new_dict)


id_grade_dict = {"Dan": [],
                 "Shir": [],
                 "Rotem":[],
                 "May" : [],
                 "noam": [],
                 "Matan": []}

keys_list2 = list(id_grade_dict)

for i in range(len(keys_list2)):
    if keys_list2[i] == new_dict[i][0]:
        id_grade_dict[i][0] = new_dict[i]
        id_grade_dict[i][1] = new_dict[i][1]

print(id_grade_dict)
'''