#    indexing

str = "Ruhi Ali"
ch = str[0]
ch2 = str[7]
print(ch)
print(ch2)
print(str[5])

# Slicing      (part of the data)

str = "Universe"
ch = str[0:5]
print(ch)       #0r
print(str[1:4])
print(str[2:len(str)])
print(str[:5])             #mean [0:5]
print(str[3:])              # mean len(str)
print(str[::2])             # starting and stopping not just gap 2
print(str[:5:3])            # stopping and gap
print(str[2:6:3])          # strat stop and gap
print(str[::-1])            # reverse
print(str[:8:-1])

# slicing  negative index       ( from strating the index +ve  and from backward the index -ve  this -ve index just in slicing)
# example  A  p p  l  e
#         -5 -4 -3 -2 -1
print(str[-5:-2])

# String Function             
str = "i Am your owner"
print(str.endswith("ner"))      # True      (Our string end with this word or not)
print(str.endswith("wer"))      #False
print(str.capitalize())        #  to be true sentence capitalization  
str = str.capitalize()          # both valid
print(str)
print(str.replace("your" , "AI"))    # replacing words or letters in a sentence
print(str.replace("r" , "s"))
print(str.find("r"))          # finding woeds or letters whichbcomes first in  a sentence
print(str.find("your"))
print(str.find("T"))          # when we sereach for a word or letter which not exist so py print "-1" which means not exist .
print(str.count("o"))         # count for a word or letter how many times repeat in a sentence.
print(str.count("your"))


#........

a="Comupter Sciece"
print(a)
print(a.startswith("y"))        # string start from
print(a.startswith("S", 9,12))  # also set range 
print(a.endswith("e"))          # string end
print(a.endswith("r" ,2,8)) 
print(a.swapcase())            # capital letters convert into samll and small into capital.

b="     Computer     "
print(b)
print(b.strip())   # removing somthing from strings.

c="ruhi&star"
print(c.split("&"))    # seperate strings value from any symbol.

d="helloo .This is Ruhi here. today's a good day . wish you all the very best, Thanku"
print(d.split("."))

e="Ruhi"
print(e.ljust(15 ,"*"))              # somethings add or space in the left side of the string.

x= e.rjust(20,"-")                   # as as inthe right side of the string.
print (x, " is my favorite person")

a=" This is Ruhi . Ruhi's work smart"
print(a.replace("Ruhi", "Alia"))       # somwthing replace
print(a.rindex("Ruhi"))
print(a.rfind("Ruhi"))               # rindex and rfind work same findin index of string
print(a.rfind("Ruhi" ,2,13))         # also find in range
print(a.rindex ("s", 5,10))


z= "f.r.i.e.n.d.s"
b = z.replace(".", "")
print(b)

a="Ruhi Is the best"
print(a[::-1])

a= "Ruhi110"
print(a.isdigit())
print(a.isalpha())
print(a.isalnum())
print(a.isdecimal())
print(a.istitle())         # show that every word begins with a capital letter or not


# List

list = [32,56,7,89,70,12,34,77,89,90]
print(list)
print(type(list))
print(len(list))
print(list[6])
print(list[0])

student = ["Ali", 89, "islambd", 0.89 ]        # in list we can save different type of data not same only.
print(len(student))
print(student[0])                             # indexing
print(student[3])

# List Slicing 

list = [32,56,7,89,70,12,34,77,89,90]
print(list)
print(type(list))
print(list[1:5])
print(list[:4])
print(list[2:])
print(list[-4:-1])


# list append method  (in append add only one string or num)
list = [5,9,7]
list.append(6)
print(list)
# Sort method  (ordering , in accending order or decending order) list sort by dafult accending order.
list.sort()
print(list)
# sort reverse true method
list.sort(reverse=True)        # if you write in accending this change into decending and visversa.
print(list)
# reverse method           (not keep accending decending but it completly reverse the list without order)
# list = list.reverse()
print(list.reverse())
print(list)
# insert method
list.insert(9 , 8)
print(list)
# remove method
list.remove(7)         # simply degit 7 remove (if u want to remove string or num u put the name)
print(list)
# pop method
list.pop(1)            # delete a number which index 1 (for removing somthing put the index not name)
print(list) 
# clear method , whole list will be clear
list.clear()
print(list) 

# copy of list

a = [1, 2, 3, "ali"]
b=[]
print(b)
b= a.copy()
print(b)
print(a.index("ali"))
# in extend method add one list in another and shows as a one list
c = ["Ruhi", "Alia" , 5]
a.extend(c)
print(a)

#...
fruits = ["mango" , "banana" , "lichi" , "apple"]
fruits.append("orange")
fruits.sort()
fruits.reverse()
fruits.insert(1 , "tomato")
fruits.remove("lichi")
fruits.pop(2)
print(len(fruits))
print(fruits) 

#....
#append list1 in list2 by for loop

l1 = [6,8,0,9]
l2=[]
for i in l1:
    l2.append(i)

print(l2)
print(l1 , l2)
print( l1 , "\n" , l2)     # \n mean next line\
# comprehension method of list

l3 = [i for i in l1 if i > 6]
print(l3)

# Swap elements   ( exchange place)
a= ["Ali" , 123 , "Ruhi"]
a[1] ,a[2] = a[2] , a[1]
print(a)

# multipy num of list
b = [ 4, 7 , 9 ,67 ,89]

mul = 1
for i in (b):
    mul*=i
print(mul)

# smallest and largest value finding in list
b.sort()
print(b)
print("lagest value is", b[-1])
print("smallest value is", b[0])


#     Tuple      
# not append not remove not change   , tuples are imutibale just like strings (mean cannot change), not remove , append, update
tup = (2, 4, 8 , 9)
print(tup)
print(type(tup))
print(tup[0])
print(tup[3])
# also creat a single value tuple , in tuple (,) must after a single digite , if not than this like a integer
tup = ( 2 ,)
print(type(tup))
print(tup)

tup = (5)              # without (,)  shows an integer
print(type(tup))   

tup = ("Hlw",)
print(tup)
print(type(tup))
# slicing in tuple
tup = (1 , 3,3 ,5 ,7, "odd")
print(tup)
print(type(tup))
print(tup[0:3])     # etc all possible slicing
print(tup[1::2])
print(tup[::-1])
# tuple methods
#finding a place of num that where 
print(tup.index("odd"))      # this string or num index
print(tup.count(3))      # how many times repeat a num
# with for loop
for i in tup:
    print(i)
# with range for loop
for i in range(len(tup)):
    print(tup[i])
# with while loop
i = 0
while i < len (tup):
    print(tup[i])
    i += 1

# conversion of tuple
a = ("alia" , "hashma", "Ryan")
print("before conversion" , type(a))

# a = list(a)
# print("after conversion", type(a))
# a.append("Ruhi")
# print(a) ?

a = tuple(a)
print(type(a))

#close