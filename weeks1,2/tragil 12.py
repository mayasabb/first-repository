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


