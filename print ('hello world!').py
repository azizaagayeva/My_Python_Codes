name = 'lov catz'
print (' we '+ name +('!'))
text = 'catz'
#strings: when we put name it gets replaced with whatever we write on the code
decimal = 10.5
number = 10
#notes
has_money = True
coordinates = (2,5 , 1,5)
names: ('Manon','camilla','celestine')
# doesnt actually do anything >3
unique={ 1,3,5,7,9 }
print (unique)
users = {'Marie': 1, 'Kat': 2} #shows the users 
number = '150'
print(10 + int(number))
print(float('123.456'))
age : int= 25
first_name:str ='lukaz'
print (age)

import datetime
import time

# Get user input

first_name = input("Enter your name: ")
last_name = input("Enter your surname: ")
birth_year = int(input("Which year were you born in? "))

# Calculate age

current_year = datetime.date.today().year
age = current_year - birth_year

# Display the result

print(f"\n{first_name} {last_name} is {age} yrs old")
time.sleep(30)