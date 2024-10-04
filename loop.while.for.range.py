# Loops in python     " while loop"   when a loop run with some conditions or stopping then use this while loop

count = 1           # called iterator   this process called iteration .
while count <=6 :
    print("Ruhi")
    count += 1
    
print(count)

#...
R = 0                #  start from 0 or 1 same
while R < 10:
    print("Hlw World", R)
    R += 1

print(R)

#...
num = -2
while num <= 7:
    print(num)
    num += 1

#....
i = 7
while i >= -5:
    print(i)
    i -= 1

#....
n = 1
while n <= 10:
    print(5*n)        # tabale in loop method , any tabale instead of 5 place.
    n += 1

#.... creat list with a loop
num = [1,2,5,77,8,20,78,90,4,3,2]

indx = 0
while indx < len(num):
    print(num[indx])
    indx += 1

#...... tuple with a loop      
agency =  ("tigger", "loin" , "jarraf", "cat" , "dog" , "elephant", "human" )

A = 0
while A < len(agency):
    print(agency[A])
    A += 1

#....general Q
racecar = ["farrari" , "limborgini" , "GLI" , "civic"]

win1 = "limborgini"


i = 0
while i < len(racecar):
    if (racecar[i] == "farrari"):
        print("yeah we win")
    elif (racecar[i] == "limborgini"):
        print("ohhho")
    else:
        print("no")
    i += 1
    
#.....
tup = (1 , 0.7 , 7 ,90 , "Ruhi" , "Ali")

x = "Ruhi"

i = 0
while i < len(tup):
    if (tup[i] == x):
        print("found it at index" , i)
        break                               # break use for stop other print , if tup find then break mean nothing print after that.
    else:
        print("finding...")
    i += 1

print("end loop")

#....
i = 0
while i <= 6:
    if (i == 4):
        i += 1
        continue         # skip , mean continue opposit to break , and continue cammand also skip beacause with and without same.
    print(i)
    i += 1

#........
i = 0
while i <= 12 :
    if ( i % 2 != 0):        # even or odd num print
        i += 1
    print(i)
    i += 1

#.....
i = 1
while i <= 12:       # also creat add or even num like this .
    print(i)
    i+= 2  

    #....
i = 1
while i <= 20:
    if (i % 5 == 0):
        i += 1
    print(i)
    i += 1

# while true

while True:
    num1 = int(input("enter a number here:"))
    num2 = int(input("enter another number here:"))

    print ( num1 * num2)
    repeat = input("do you want to stop the program:")
    if repeat == "yes":
        break 

n = 1
while n <= 5:
    if n == 3:
        print ("midd val")
    else:
        print(n)
    n += 1   


# 'for loop'     when on data treverse ( treverse mean on data one by one work) then use for loop.

list = [ 1, 7 ,8 ,9, 0.9, 5] 

for a in list:
    print(a) 

#......
tup = ("red", "blue" , "yellewo" , "orange")

for val in tup:
    print(val)

#.....
str = "AliaHashma"         #  treverse on characters of string

for char in str:
    print(char)
else:
    print("end")            # whensomething print after loop this is optional , if we are not use else same thing print

#.....
str = "Engineering"

for chr in str:
    if (chr == "i"):
        print("i found")
        break                   # in break case thi difference else print.
    print(chr)
else:                           # in this case end not print but if we don't use else and simply print end so print.
    print("end") 

#.....
list = (1,2,3,4,5)

x = 3
idx = 0

for val in list:
    if (val == x):
        print("found x at" , idx)        # this is linear sreach.
        break
    idx +=1
    print(val)

# Range                    range(start , stop , step)    stop must and starting and step val optional, by dafult step 1

seq = range(5)        # (stop condition)            # ending number not incluted and starts from zero

for i in seq:
    print(i)   

#...
for i in range(2 , 7):      # range (start and stop)   from 2 to 6
    print(i)

for i in range(2 , 7 , 2):    # range ( start, stop , step)  step mean gap
    print(i)

for i in range(0 , 10 , 2):     # print even num
    print(i)

for i in range(10 , 0 , -1):
    print(i)

for i in range(1 , 11 ,):
    print(3*i)       # table of 3

for i in range( 5, 12,3):
    pass                      # pass use  for skip the loop

#....
n = 12

for i in range (1 , 11):
    print (n, "x", i, "=", n*i )        # table formate

#...squres
for i in range (1 , 15):
    print ( i ** 2)


#....
for i in range (1 , 8):
    if i == 4:
        print("4 this is the mid value")
    else:
        print(i)

#...
for i in range (1 , 50):
    if i % 5 == 0 and i % 2 == 0:        # mean we want to print common divisble of 5 and 2
        print(i)   


# nested loop
for i in range (1 ,4):
    for j in range (1 , 11):
        print (j , end = "")      # for this inner loop  , end = ""mean print in one line
    print()                     # for first loop print( ) mean null

#....
for i in range ( 1, 7):          # first loop shows number of rows
    for j in range (1 , i+1):     # inner loop shows num of columns
        print(j , end = " ")
    print ()

#.../
for i in range (1 ,5):        # rows
    for j in range (1 , 5):    # columns
        print( j , end = " ")
    print()

#...
for i in range (1, 6):
    for j in range (1, i+1):
        print("*", end = "")
    print()

#....
for i in range (1 , 7):
    for j in range (2 , i+1):
        print (i , end = " ")       # now print i (rows)
    print()

#.....
for i in range (1,5):
    for j in range (5 , i, -1):
        print ("$" , end = " ")
    print()

#....
for i in range (1, 6):
    for j in range (6, i , -1):
        print (i , end = " ")
    print()

#...
for i in range (1, 7):
    for j in range (6, i , -1):
        print(" ", end = " ")
    for k in range (i):
        print ("?" , end = " ")
    print()

#...
for i in range(1, 6):
    for j in range( i , 0 , -1):
        print(j, end = " ")
    print()

#...
for i in range(1 , 7):
    for j in range (1, i+1):
        print("*",end = " ")
    print ()
for i in range( 6, 0 , -1):
    for k in range (0, i-1):
        print("*", end = " ")
    print()

# fibonaci series ,   mean 0,1,1,2,3... mean 0+1  is 1, 1+1 is 2 , 1+2 is 3 , 2+3 is 5 up to ...so serise is 0,1,1,2,3,5,8..

a = 0
b = 1
print(a)
print(b)
for i in range(2, 15):
    c = a+b
    a = b
    b = c 
    print(c)

# palindrome   (method of palindrome)

n = 323
copy = n
re = 0
while n >0:
    dig = n%10
    re = re*10 +dig
    n = n // 10
if re == copy:
    print("palindrome")
else:
    print(" not")

#.....
num = int(input("enter a numbr here for checking palindrome:"))
temp = num
rev = 0
while num > 0:
    dig = num%10
    rev= rev*10 + dig
    num = num // 10

if rev == temp:
    print("it is a palindrome")
else:
    print("not a palindrome")

#....another simple method of palindrome
a= input("enter something here for checking palindrome:")
rev = a [::-1]

if a==rev:
    print("it is palindrome")
else:
    print("it's not palindrome")

# short hand for loop , for iteration (mean one by one value show of list)

a=["apple", "mango" , "banana" , "orange"]
[print (i) for i in a]