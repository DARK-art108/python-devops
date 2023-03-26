# a = "hello"
# b = 'world'
# x = a+b #concatenation
# print(x)

# hello --> aello

## hello --> h --> 0, e --> 1, l --> 2, l --> 3, o --> 4 --> indexing
## hello --> -5, -4, -3, -2, -1 -> reverse indexing
# a = "hello" --> list or array
### [1,2,3,4,5] --> list or array --> ['h','e','l','l','o']
# a[0] = "a"
#print(a)


## built type functions -> list, tuple, set, dictionary
## TyPe casting -> int(), float(), str(), list(), tuple(), set(), dict()
# a = "hello"
# lst = list(a)
# print(len(lst))
#float--> decimal --> 2.3, 4.5555
# a = 2
# print(type(a))
# s = float(a)
# print(type(s))
# print(s)
# p = str(s)
# print(type(p))
# print(p)


# b = 9
# print(b-p)

# a = True
# b = False

# print(a != b)
# print(a and b)
# print(a or b)
# print(not a)
# print(not b)
# print(a & b)

## input function

# a = int(input())
# b = int(input())
# print(a+b)

## string formatting f-string

# a = "hello"
# b = 10

# print(f"this is {a}, I have {b} apples")


## if else
# a = 2
# b =3
# if a>b:
#     print("a is greater")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("b is greater")


# a = 3 
# b = 4
# c = 5

# a,b,c = b,a,d
# print(a,b)

## for loops
## start, stop, step
# for i in range(1, 11, 2):
#     print(i)

## nested for loop

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")



## functions

# def add(a, b):
#     return a+b

# t = 2

# def add(a, b) -> int:
#     return a+b


# a = int(input())
# b = int(input())
# print(add(a,b))



# def func():

## Imports


# import math
# from math import sqrt
# from math import sqrt as sq
# import random

# random_num = random.randint(1,10)
# print(random_num)

## C++ -> #include <iostream>
#include<bits/stdc++.h>

## C -> #include <stdio.h>


## typing module
## Union[X, Y] means either X or Y.
# from typing import List, Tuple, Set, Dict, Union, Any, Optional

# def add(a: int, b: int) -> Union[int, float]:
#     return a+b

# def add(a: int, b: int) -> Any:
#     return a+b




# ~ Dict, Hashmap, Maps, Unordered Maps, Associative Arrays

# Dict/Maps
# uuid -> unique id for each user

#Maps is a data structure which stores data in key-value pairs. It is used to store data like a phonebook. In phonebook, we have names as keys and phone numbers as values. Maps are also known as associative arrays or dictionaries in other languages.
# zomato/ swiggy
# zomato = {
#     "name": ("Rahul"),
#     "order-id": "iu2311huhjksdbcv34647",
#     "items": ["pizza", "butter paneer", "coke", "frech fries", "chicken nuggets"],
#     "address": "xyz",
#     "phone": 1234567890,
#     "live-location": {"lat": 12.123, 
#                     "long": 12.123,
#                     "weather": 
#                     {"city": ["kanpur", "delhi"],
#                     "temprature": 34
#                         }
#                     },
#     "order-status": "in-progress"
# }

# print(zomato.values())




# {key:value} -> 
# x = {name: Ritesh} --> x.name ---> x.values() ---> x.keys()
# for i in x.keys()  #traversing in an array  [1,2,3,4,5,6]


# arr = [1,2,3,4,5,6]
# for i in range(len(arr)):
#     x = 4
#     if i=4 --> print(idx of 4)
#     else 4 is not present

# for i in x.keys():
#     print(x.values()[i])


#class

# class hello:
#     pass



# next code block

## Parent class  -> Child class -> Grandchild class


class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
labrador = Dog()

# access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()

# call subclass method 
labrador.display()









