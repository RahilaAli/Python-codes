# Q1) Consider the given expression: not True and False or True .
"""(not Ture)and False or True         (not True mean false)
    (False and False) or True          ( "and" operator says , if at least one value is false the result is false)
    False or True                       ("or" operator says that if one value is true the  result will be True)
    S0 the answer is "True"""



# Q2    .....writ a code for even or odd numbers.
num = 15
rem = num %2

if (rem == 0):
    print("even")
else:
    print("odd")
#Q3.....write a code for three numbers in this one number which greater or smallar than others.
a = 55
b = 45
c = 65

if ( a > b and b < c):                    # if first statment true so print first 2nd true or false not concerned
    print("b is the smllest num")          # in this case both are true but prefer 1st
elif ( c > b and c > a):
    print("c is the greatest num")
else:
    print(" not valid ")

# Q4 ......write a code for a number which is divisible by 7 in a conditonal statment
num = 49
rem = num % 7

if( rem == 0):
    print("multiple of 7")
else:
    print("not")
    
#Q5...write a code for a list of heros
myheros = []
her1 = input("enter a 1st hero name:")
her2 = input("enter a 2nd hero name:")
her3 = input("enter a 3rd hero name:")

myheros.append(her1)
myheros.append(her2)
myheros.append(her3)

print(myheros)

# Q6 write a palindrome of elements in a list.       ( palindrome mean which same from strats or from end  that is maam , racecar,)
# for check palindrome in a list first we copy a list and write reverse the copy list and check it with orignal list that is same.

list1 = [1 , 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if ( copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

# Q7 creat billing system for supper market

while True:
    name = input("enter customer name:")
    total = 0
    while True:
        print (" enter price and quantity")
        price = float (input("enter price :"))
        quntity = float(input("enter quntity:"))
        total += price * quntity
        repeat = input("do you want to add more items? (yes/no):")
        if repeat == "no" or repeat == "No":
            break
    print ("." * 50)
    print ("Name:", name)
    print ("amount to be paid:" , total)
    print ("^^^^^Happy shopping^^^^^")

    repeat1 = input("do you want to go to next customer ? (yes/no):")
    if repeat1 == "no" or repeat1 == "No":
        break
print ("-" * 30)

# Q8 if num is prime or not

num = int(input(" entr a number here:"))
if num <=1:
    print("not prime")
else:
    for i in range(2,num):
        if num% i != 0:
            print("prime")
            break
        else:
            print("not prime")

#Q9 first 20 numbers and their square

for i in range (1 , 21):
    print(i, i**2)

# Q. find vowels in a string

a= input("enter something here we check in vowels:")
vowels=0

for i in a :
    if i== "a" or i =="e" or i =="i" or i =="o" or i == "u":
        vowels +=1

print(" the number of vowels in a string are " , vowels)
