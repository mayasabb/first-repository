'''
print("Enter a number")
x=float(input())
y=int(x)
print(y)
'''
import datetime
import math
'''
print("Enter a number")
x=float(input())
math.floor(x)
print(math.floor(x))


print("Enter a number")
x=int(input())
print(math.sqrt(x))

print("Enter two numbers")
x=int(input())
y=int(input())
print(math.pow(x,y))

print("Enter a number")
x=int(input())
y=math.e
print(math.pow(y,x))

print("Enter a number")
x=int(input())
y=3*(math.tan(x))
z=(math.cos(x))**2
print(y-z)
'''

books=18
notebooks=23
pens=9
print("How many books did you buy?")
a=int(input())
print("How many notebooks did you buy?")
b=int(input())
print("How many pens did you buy?")
c=int(input())
x=datetime.datetime.now()
print("Today's date:",x)
d=18-a
e=23-b
f=9-c
print("You have",d,"books,",e,"notebooks,and",f, "pens left" )

h=d+4
h1=e+2
h2=f+5

number_of_books=int(input("How many books did you buy?"))
number_of_notebooks=int(input("How many notebooks did you buy?"))
number_of_pens=int(input("How many pens did you buy?"))

the_year_of_purchase=int(input("Enter the year:"))
the_month_of_purchase=int(input("Enter the month:"))
the_day_of_purchase=int(input("Enter the day:"))
the_date_of_purchase=datetime.datetime(the_year_of_purchase,the_month_of_purchase,the_day_of_purchase)

number_of_books_bought=int(input("How many books did you buy?"))
number_of_notebooks_bought=int(input("How many notebooks did you buy?"))
number_of_pens_bought=int(input("How many pens did you buy?"))

the_year_of_purchase_=int(input("Enter the year:"))
the_month_of_purchase_=int(input("Enter the month:"))
the_day_of_purchase_=int(input("Enter the day:"))
the_date_of_purchase_=datetime.datetime(the_year_of_purchase_,the_month_of_purchase_,the_day_of_purchase_)

print("If true the purchase that happand in {} is the latest one ".format(the_date_of_purchase))
print(the_date_of_purchase>the_date_of_purchase_)

m=h-number_of_books-number_of_books_bought
l=h1-number_of_notebooks-number_of_notebooks_bought
k=h2-number_of_pens-number_of_pens_bought
print("You have {} books {} notebooks, and {} pens left".format(m, l, k))









