# How to reverse a string
'''
string = "Hello, this is Arpit Garg"
print(string)

a = string.split()
c = []
print(a)
for i in a:
    rev = i[::-1]
    c.append(rev)
print(c)
rev_string = ' '.join(map(str, c))
print(rev_string)
'''

# Remove Repeatative Numbers from an Array(List)
''' 
my_list =  [1,2,3,4,5,6,7,2,3,1]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
'''

# Lambda Functions
'''
my_func = lambda x: x*x
print("square is :", my_func(2))
'''

# Generator Functions

''' 
def gen():
    yield 1
    yield 2
    yield 3

values = gen()
print(values.__next__())    #For values
print(values.__next__())  
print("-------------")  
#yield basically a type of return which is used to create generator it not get terminated after execution of a program

def gene():
    n = 1
    while n <=10 :
        sq = n*n
        yield sq
        n += 1
val = gene()
for i in val:
    print(i) 
'''

# Multithreading
'''
from threading import *
from time import sleep

class func1(Thread):
    def run(self):
        for i in range(50):
            print("Func1 ..")
            sleep(2)

class func2(Thread):
    def run(self):
        for i in range(50):
            print("2 ..")
            sleep(2)

t1 = func1()
t2 = func2()
t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

#Here basically multiple threads are working simultaneously.
# Here Three threads are working-
# 1. main thread
# 2. t1
# 3. t2
'''

