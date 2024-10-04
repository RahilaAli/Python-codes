# Input in python
#string input'
name = input("name:")
print(name)

#int input
age = int (input("age:"))     # in this write of the type before input
print(age)

#float input
wieght =float(input("wieght:"))
print(wieght)

print(type(wieght))

print("my name is", name, "and i am", age,"years old" ,"and my wieght is" , wieght ,)

name = input("name:")
print("welcome", name)


# Calculate simple interest
p= float(input("p:"))     # p for Principle
r= float(input("r:"))     #r for rate
t= int(input("t:"))        # t for time
print(p*r*t/100)          # formula (p*r*t/100) 


# Conditional Statments  (if-elif-else) in small leter this is the syntax

"""if (Condition):
    Statment1       (four spaces gap)
elif(Condition):
    Statment2
else:                 (not checke a condition)
    StatmentN  """

#Python is an indentation language , mean proper spacing must in some cases.

 #Triffic light code

light = input("light:") 

if (light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")
 
 #general Ruhi's statment

Ruhi = input("Ruhi:")

if (Ruhi == "i am ok"):
    print("i am not ok")
elif (Ruhi == "its ok"):
     print(" something is fishee")
elif(Ruhi == "i don't need "):
    print(" i need")
elif(Ruhi == "go away"):
    print("come here")
elif(Ruhi == "craying"):
    print("leave me alone")
else:
    print("go away")

# in single line if statment write, this is called ternary operator

# format:   variable = "value" if (condition) else"value"

food = input("food:")
eat = "yes" if food == "burger" else "no"
print(eat)                                                    # short format of if condition.

car = input("car:")
print("ohoo yeah") if car == "fararii" or car == "limborgini" else print("no way") 

# clever if or ternary operator
#format variable = (false_val, true_ val) [condition]   
# (in this condition write in [] brakets and 2nd value our right  value, First our wrong)

age= int(input("age:"))
vote = ("no" , "yes") [age >= 18]
print(vote , "You Give Your Vote.")  

sal = float(input("salary:"))
tax = sal*(.5 , .2) [sal <=80000]
print(tax , "tax cut from Your salary")     

# Nesting (mean in one statment also write other statment )

fan = "off"
if (fan == "off"):
    if(fan == "not work"):
        print("destroy")
    else:
        print("light has been gone")
else:
    print("destroy")
#........


A = (input("A:"))
Z = input("Z:")
if ((A == 2 or A == 4) and Z == "R"):
    print("win")
if ((A == 2 or A ==5) and Z == "S"):
    print("medium")
elif(A == 3 and Z == "S"):
    print("loser")
elif(A == 5 or Z == "R"):
    print("nuetral")
else:
    print("none")   #?

    # creat area calculator
print("    AREA CALCULATOR   ")
print (""" press 1 get the area of square
press 2 get the area of rectangle
press 3 get the area of circle 
press 4 get the area of triangle""")         #  use  triple (") for many lines print in one statment 

choice = int(input("enter a number between 1 - 4 :"))

if choice == 1:
    side = float(input("enter the lenght of one side:"))
    area = side **2
    print ("the area of square is", area)

elif choice ==2:
    length = float (input("enter the length of the rectangle:"))
    width = float (input("enter the width of the rectangle:"))
    area = length * width
    print(" the area of rectangle is", area)

elif choice == 3:
    radius = float(input("enter the radius of the circle:"))
    area = ((22/7) * (radius**2))
    print ("the area of the circle is", area)

elif choice == 4:
    base = float (input("enter base of the triangle:"))
    hieght = float (input("enter hieght of the triangle:"))
    area = ((1/2) * base * hieght)
    print ("area of the triangle is", area)
else:
    print("invalid")

# Digits of numbers.

num = int(input("enter a number here up to 4 digits:"))

if num >= 0 and num <= 9:
    print ("it is a single digit number")

elif num >= 10 and num <= 99:
    print ("it is a double digit number")

elif num >= 100 and num <= 999:
    print(" it is a triple digit number")

elif num >= 1000 and num <= 9999:
    print (" it is a four digit number")
