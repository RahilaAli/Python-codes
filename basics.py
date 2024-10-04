#variable and types practice

name="Rahila"   #string    
age=20          #integer   (all +ve,-ve,zero)
price="infinit"  #string
age3=price        #string
time=4.5           #floating  (all decimals)
rate="34"          #string ;   ( in  "" all of thing are called string)
man=False           #boolean     (the true and false are boolean)
woman=True          #boolean     (nte; the True and False must strat from capital)
b=None              #empty    (None also strats from capital)       (because of these are the key words)

print("my name is ",name)
print("my prirce is",price)
print(age3)
print(man)
print(b)


print(type(age))
print(type(name))
print(type(price))
print(type(age3))
print(type(time))
print(type(rate))
print(type(man))
print(type(woman))
print(type(b))

 #python is a typed language,(type lang are two type that is ; implicit and explicit)
 #so python is a implicit type. who say type of our code atomatically , we are not mention.

#sum,prod,div etc
a=45
b=44
sum=a+b
print(sum)
pro=a*b
print(pro)
div=a/b
print(div)

#strings addition and length of string
str1 = "Ruhi"
str2 = "Ali"
print (str1 + str2)

print(len(str1))
print(len(str2))

#Expression Execution

a,b=3,8
txt="Ali"
print(3*txt*8)      #mean init value multiply with string work like reapetation (reapet the string value of a,b time)

a,b="4",5
txt="@"
print((a+txt)*b)     #Means tow strings are plus like this "4@" can operat with, this is called "concatenation".

a,b,c=2,5,8
d=7
e=10
print(a+b-c*d/e)     #means numiric value can operate all arithmatic operation (+,-,*,/)

a,b=5,7.0
print(a+b)
c=a*b
print(c)    #Means that arithematic exprission with integers and float will result in "float"

a,b=4,2
print(a/b)
a,b=3,2
c=3/2
print(c)    #means that division of two integers will be "float"

a,b=2,3
c=a//b               #integer division or floor.
print(c,a/b)    # integer division is that type of divison in which  result round off into its small value 
                # that is "0.999" convert into "0", or 1.2 convert into 1 and 5.5 convert into 5,and 3 convert simply in 3 etc.
a,b=-3,12       # so simply integer divison mean floor, and " floor gives closest intiger which is lesser then or equal to float value"
c=a//b                
print(c)             # now in this case integer division with float or int will gave int displayed as float.

a,b=-5,6
print(a%b)     # % mean remainder.
                # so remaider nagative when denominator is nagative other wise +ve.
print(b%a)
print(a**b)     # **mean square

# results boolean values
a=78
b=45

print(a == b)  # False       #(these operators are ralational or comparesion operators)
print(a != b)  #True
print(a > b)   #True
print(a< b)    #False
print(a <= b)   #False

# assignment operators   ( =, +=, -=, *= , %= , **=)
num = 20
#num = num + 10 ,    # instead of this we can write (num +=10   , this += is assignment operator)
num += 10
print(num)

#logical operator ( not, and, or)
a= 20
c= 50
print(not False)
print(not (a<c))   # ( not gives opposite value)

val1 = True
val2 = False
print( val1 and val2)     # only True print if both are True
print(val1 or val2)       # True print if one of these are True


# Binary mean 2 , that is 1 and 0, 1 mean on and 0 mean off
# if we find binary of 10 that is 10 / 2 reminder is 0 than 5 / 2 reminder 1 etc 
print(bin(10))
print(bin(15))

a = 10
b = 8

print (a & b)       # & mean a * b
print (a | b)       # | mean a + b
print (a ^ b)       # ^ mean a - b
print (10 >> 2)     # >> mean zero fill left shift ,( mean 2 last digits of bin of 10 cancel
                     # and add 2 zero in first that is 1010 become 0010 )
print (10 << 2)      # zero fill right shift

# membership operators ( in , not in)
a = "hello"
print("e" in a)         # in mean exist
print("r" in a)
print("l" not in a) 
print("r"not in a)     # not in mean not exist


#close