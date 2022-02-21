import math
from datetime import datetime
from dateutil import parser

print("Hello world!")

Name = input ("Enter your name: ")
print("Hello,", Name)

print("Your name has", len(Name), "letters. Factorial of this number is", math.factorial(len(Name)))

date = parser.parse(input("Please, enter your birth date in format (DD.MM.YYYY):"))
today = date.today()
age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
birth_date = date
time_difference = today - birth_date
print("Today is "+str(today.strftime('%d.%m.%y'))+", you are "+str(age)+" year old.(", time_difference,")")
