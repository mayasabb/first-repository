'''
result=0
for i in range(3):
    x= int(input("enter a number"))
    result += x
print(result)
'''
num=int(input())
sum=0
while num != -1:
    sum += num
    print("put in a number, -1 to exit")
    num=int(input())
