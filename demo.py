
# 01 comments

# print("hello world")
# print("this is in comments")
# """
# print(12)
# print(11)
# """
# hello
# world
# march

# 02 variables name

# name 
# name_name
# nameName
# _name
# NameName
# name1st

# name name 
# $name 
# 1stName

# 03 variables for string 

# name = "aslam"
# print(name)

# name1 = "atif"
# name2 = "asif"

# print(name1,name2)
# print(name1)
# print(name2)

# 04 variables for numbers 

# num = 23 / 8
# num2 = 90
# print(num,num2)

# 05 numbers r strings  concatination

# name = " aslam"
# name2 = " atif"

# num1 = 12
# num2 = 34

# print(name + name2)
# print(num1 , num2) 

# 06 math familiar/ unfamiliar operator 

# a = 12
# a -= 45
# print(a)

# 07 Math ambiguity 

# num = (3 + 4) * 5
# print(num)

# 08 inputs 

# x = input("enter the name? ")
# print(x) 

# 09 data types 

# name = "Shoaib"
# num = 34
# print(type(name),type(num))

# 10 type casting 

# name= int("56")
# name= float("56")

# num = str(45.00)
# print(type(name))
# print(type(num))


# >>---------------------------------------- 

# data types

# a = "hello world"
# print(type(a))

# b = 45
# print(type(b))

# c = 45.00
# print(type(c))

# d = True
# print(type(d))

# e = [1,2,3,4]
# print(type(e))

# f = {"name":"shaoib"}
# print(type(f))

# g = {1,2,3,4}
# print(type(g))

# h = frozenset({1,2,3,4})
# print(type(h))

# i = None 
# print(type(i))

# j = (1,2,3,4,5)
# print(type(j))

# 11 string operations

# st = "string Hello {price} "
# print(st.capitalize())
# print(st.casefold())
# print(st.format(price= 40))


# 12 escape character

# escap = "hello world \t \t hi hello world"
# print(escap)


# 13 if statement 

# x = "s"
# if( x == "m"):
#     print("your true value")
# else :
#     print("your false value")

# y = 12
# if( y <= 11):
#     print("you pass")
# else:
#     print("fail")

# h= 4
# a= 11
# e= 12

# if(h == 5):
#     print("pass")
# elif(a ==18):
#     print("pass")
# elif(e == 12):
#     print("pass")
# else:
#     print("failed")

# if( h == 5 and a == 18):
#     print("Pass")
# elif(a == 18 and e == 12):
#     print("Pass")
# elif(h == 5 and e == 12):
#     print("Pass")
# else:
#     print("Failed")

# if( (h == 5 and a ==18) or (a == 18 and e==12) or (e ==12 and h ==5)):
#     print("Pass")
# else:
#     print("fail")


# h= 4
# a= 18
# e= 12

# if(h == 5):
#     if(a == 18 or e ==12):
#         print("Pass")
#     else:
#         print("Failed")
# elif(a == 18):
#     if(h == 5 or e == 12):
#         print("Pass")
#     else:
#         print("Failed")
# elif(e == 12):
#     if(h == 5 or a == 18):
#         print("Pass")
#     else:
#         print("Failed")
# else:
#     print("Failed")


# 15 lists


# ls = [1,2,3,4,5]

# 16 add lists and change
# 17 lists slices
# 18 delete/remove from lists element/s

# ls = ["j","L"] + ls + ["K"]
# ls.append("K")
# print(len(ls) -1)
# ls.insert(1,"KALAM")
# print(ls)

# del ls[0]
# del ls[0]
# del ls[0]

# ls.remove(3)

# slc = ls[2:]
# print(slc)


# //////////////////////////////////////////
# 19  for loop , while loop 

# ls = [1,2,3,4]
# print(ls)

# for y in ls:
#     print(y)

# x = 1
# while(x <= len(ls)):
#     print(x)
#     x +=1

# for x in range(3,31,3):
#     print(x)

# ls = ["islamabad","jaranwala"]
# city = input("Enter your city: ")

# if city in ls:
#     print("your city is cleanest: ")
# else:
#     print("dirty city")



# 20 iterator and iterables in python

# ls = [1,2,3,4]
# ls1 = iter(ls)

# print(next(ls1))
# print(next(ls1))
# print(next(ls1))
# print(next(ls1))

# 21 tuples
# tup = ("hello","world")
# x = list(tup)
# x.insert( 1,"!")
# x.remove("hello")
# del x[0]
# x.pop(0)
# y = tuple(x)
# print(type(x))
# print(tup, x,y)

# 22 loop in tuple 


# tup = (1,2,3,4)
# for x in tup:
#   print(x)

# tup = ("hello world",)
# print(type(tup))

# firstname = ["aslam","ali"]
# lastname = ["ali","khan"]
# fullname=[]

# for i in firstname:
#     for j in lastname:
#         fullname.append( i + " " + j)
# del fullname[-1]
# print(fullname)

# 23 enumerate
# tup = ["hello","world"]
# en = enumerate(tup)
# print(en)

# 24 break contineu pass if statements 

# a = 20 
# b =10

# for x in range(0,15):
#     if x == 5:
#         # break
#         continue
#     print(x)

# 25 conditional expression / ternery opertation 
# a = 70

# if a ==10:
#     print("yes")
# else:
#     print("no")

# print("A+") if (a >=90 and a <= 100) else print("B+") if ( a >= 80 and a <=89) else print("failed")



# 23  list comprehension 

# ls = ["apple","banana","mango","orange"]
# lsnew=[]

# for x in ls:
#     if "o" in x:
#         lsnew.append(x)
#         print(x)

ls = ["apple","banana","mango","orange"]
lsnew = [ x for x in ls if "o" in x ]
print(lsnew)

