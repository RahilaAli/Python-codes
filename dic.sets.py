#  Dictionary in Python

#    ( in dic any type of data store , this is a words meaning , a key value )
  # in value any type of data use but in key not use list, dic because these are mutabale changeabale, but num, float,tuple use in 
  #    key because these are not changeabale , so key are not changeabale but value changeabale
  # there is no order in dic , dic mutabale, and not creat a doublicate keys , no index in dic

inf = {
    "key" : "value",
    "name" : "Ruhi",                        # string
    "age" : 20,                             # int
    "wieght" : 59.6,                         # float value
    "is adult" : True,                        # boolen val
    "sub" : ["math" , "python" ,"java"],     # list
    "topics" : {"dic" ,"set", "matrices"},      # tuple
    34 : 56 ,
    3.4 : 98 ,  
}

print(inf)
print(inf["name"])       # by key name print but not index
print(inf[34])
inf["name"] = "Ali"       # value changeabale
print(inf)
inf["sur name"] = "Ruhi"      # add a new key and value
print(inf)
null_dic = {}        # also creat a empty dic
print(null_dic)
null_dic["werther"] = 37
print(null_dic)
 
# nested dic ( in one dic st0re other sub dic)

student = {
    "name" : "Alia",
    "age"  : 16,
    "class" : 9,
    "subjects": {
        "math"  : 98,
        "chem"  : 95,
        "phy"   : 90,
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["phy"])
print(student["age"])
# methods of dic

print(student.keys())         # just print outer keys not sub dic keys
print(list(student.keys()))       # type cast men in the form of list or tuple etc
print(len(student))
print(student.values())         # for values
print(tuple(student.values()))    # change in a tuple
print(student.items())           # items
print(list(student.items()))     # type cast into list
pairs = list(student.items())     #like index but not index
print(pairs[1])
print(pairs[3])
print(student["name"])         # if i write .get or not value same retune but .get use because if we write wrong key
print(student.get("name"))     # this not give error just print none , otherwise give error
print(student.get("surname"))   # in this case surname not exist so print none not error.
# update dic
print(student.update({"city" : "peshawar"}))
print(student)
# same as in new dic , also update a multiple keys in dic.
new_dic = {"city" : "peshawar"}
student.update(new_dic)
print(student)

# coversion of dic  
# convert dic into string
import json
Student_data = { "name" : "Alia" , "age":17 , "marks" :99}
print(type(Student_data))
data = json.dumps(Student_data)
print(data)
print(type(data))

# data = json.loads(Student_data)       # get value a single key
# print(data["age"])

# iteration in dic
student = { "name" : "Alia" , "age":17 , "marks" :99}
print(student["age"])

for  x in student:     # print all keys of dic
    print(x)

for x in student:
    print(student[x])    # gives value of keys

for x in student.values():   # also give values
    print(x)

for x, y in student.items():   # gives keys and its values both
    print(x,":", y)           # also provid : in between

x= student.get("name")
print(x)

a= student.items()       # give key , value in the form of tuple
print(a)

b= student.keys()
print(b)

c= student.values()
print(c)

d= student.copy()    # for copy
print(d)

e = student.setdefault("age" , 20)      # if we put wrong value dic print their exact value
print(e)

a= { "a" : 5 , "b":2 , "c" :3}      # accending sort by default
a = sorted(a.values())
print(a)
# keys 1 to 12 and values the keys squaring
a = {}
for i in range (1,12):
    a[i] = i**2
print(a)

# multiply
a= { "a" : 5 , "b":2 , "c" :3} 
print(a["c"])
mul = 1
for i in a:
    mul *= a[i]      # a[i] mean multiply values not keys

print(mul)

# sort keys
a= { "b" : 5 , "c":2 , "a" :3} 
a= sorted(a.keys())
print(a)



#      Sets     
# sets are mutable but set elements are immutable (not change) thats why we writ tuple in a set but not list or dic.

collection = {1, 2, 3, 1 , 2, "Hlw" }     # in set not repeat a value in this distinc different values so print only 1,2,3 , Hlw
print(collection)                         # set is un order
print(type(collection))
print(len(collection))           # length also ignor doublicate values

time = set ()      # empty set syntax    if write () than type print tuple or {} type is dic 
print(time)
print(type(time))
time.add(1)
time.add("Hlw")
print(time)
time.remove(1)
print(time)
time.discard(1)
print(time)
time.add((1,2,3,4))        # tuple , but not add list or dic
print(time)
# to remove any random value from set
time.pop()
print(time)
print(time.pop())

time.clear()         # to set empty
print(time)
# union or intersection in a set
set1 = {1, 2, 3, 3, 1, 4}
set2 = {1,2,3,5,3}
print(set2.union(set1))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

set = {2, 2.0}       # in a set 2 and 2.0 are same so print just two
print(set)
# if we print both 2 and 2.0 then
set = {2, "2.0"}      # or also "2 "  , 2.0  in this one int other val float, so print both
print(set)
# other method build in data type
set = {
    ("float" , 2.0),           # save data as a tuple with its type not in list or dic
    ("int", 2 )
}
print(set)

#iteration
a = {"apply" , 12 , "banana" , "lichi"}
for x in a:
    print(x)

b= a.copy()
print(b)

# ......
a = {"apply" , 12 , "banana" , "lichi"}
b = {"apply" ,"lichi"}
c = {"mango" , 110 , "tomato" }

print(a.isdisjoint(b))         # disjoint find  ( disjoint mean elements of set a not present in set b)
print(a.isdisjoint(c))
print(b.issubset(a))           # Subset , the set b is the part of set a 
print(a.issuperset(b))
b.update(a)                 # if b is update with a so in set b present all elements of set a also its own elements(set b)
print(b)
a.clear()      # clear set is empty
print(a)

# max and mini in a set
a = {34,67,9,8,7,56}
maximum = max(a)
minimum = min(a)
print("maximum value is", maximum)
print("minimum value is", minimum)

# for common
# a= [1,2,3,2]
# b= [2,3,4]
# c= [3,2,6]

# print(set(a) & set(b) & set(c))


# close