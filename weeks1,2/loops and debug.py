'''
#1
result=0
for i in range(1,11):
    grade=int(input("Enter your grade: "))
    result+= grade
your_score= result/10
print("your finel grade is:", your_score)

#2
sum=0
num=int(input("Enter your grade: "))
counter=0
while num != -1:
    sum += num
    num = int(input("Enter your grade: "))
    counter+=1
print(sum/counter)

#3
num= int(input("Enter a number: "))
x=0
for i in range(1,11):
    x+=1
    print(num**x)



#4
num = int(input("Enter a number: "))
x = 0
while(num**x < 500):
    print(num**x)
    x += 1
#5
x=0
num=0
while (num<=100):
    x+=1
    num+=x
    print(num)
'''
'''
#extra
#1
for i in range(2,11,2):
    print(i)

#2
num=2
times=0
while(num**times<=1024):
    print(num**times)
    times+=1
'''

#3













