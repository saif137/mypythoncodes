'''
Recursion examples
Developer: Dr. Syed Saif ur Rahman
Purpose: Educational
'''
import time

#Head recursion
def myrech(val):
    print(val)
    if val <= 0:
        return
    myrech(val - 1)

#Tail recursion
def myrect(val):
    if val < 0:
        return
    myrect(val - 1)
    print(val)

#Recursive printing
print("Head recursion : ")
myrech(10)
print("Tail recursion : ")
myrect(10)

#Iterative sum
#Both time.time() and time.clock() show that the wall-clock time passed approximately one second.
mystart = time.clock()
tsum = 0
for loop in range(101):
    tsum += loop
print("Sum is : " + str(tsum)) #5050
mystop = time.clock()
tt = mystop - mystart
print("Time take for iterative sum is: %f " % tt)

#recursive function for recursive sum
def mysum(val):
    if val == 0:
        return val
    return val + mysum(val - 1)

#recursive sum
mystart = time.clock()
print("Sum is : " + str(mysum(100))) #5050
mystop = time.clock()
tt = mystop - mystart
print("Time take for recursive sum is: %f" % tt)

#Iterative factorial
#Both time.time() and time.clock() show that the wall-clock time passed approximately one second.
mystart = time.clock()
fact = 1
for loop in range(10,0,-1):
    fact *= loop
print("Factorial of 10 is : " + str(fact)) #3628800
mystop = time.clock()
tt = mystop - mystart
print("Time take for iterative factorial is: %f " % tt)

#recursive function for recursive factorial
def myfact(val):
    if val == 1:
        return val
    return val * myfact(val - 1)

#recursive factorial
mystart = time.clock()
print("Factorial is 10 is : " + str(myfact(10))) #3628800
mystop = time.clock()
tt = mystop - mystart
print("Time take for recursive factorial is: %f" % tt)

#Iterative Fibonacci
#Both time.time() and time.clock() show that the wall-clock time passed approximately one second.
mystart = time.clock()
fib1 = 0
fib2 = 1
print(fib1),
print(" "),
print(fib2),
print(" "),
while True:
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp
    print(fib2),
    print(" "),
    if fib2 > 100:
        break
mystop = time.clock()
tt = mystop - mystart
print("\nTime take for iterative Fibonacci is: %f " % tt)

#recursive function for recursive fibonacci
#Linear
def myfib(fib1, fib2):
    if fib2 > 100:
        return
    print(fib1 + fib2),
    print(" "),
    myfib(fib2, fib1 + fib2)

#recursive Fibonacci
mystart = time.clock()
fib1 = 0
fib2 = 1
print(fib1),
print(" "),
print(fib2),
print(" "),
myfib(fib1, fib2)
mystop = time.clock()
tt = mystop - mystart
print("\nTime take for recursive Fibonacci is: %f" % tt)

#Recursive fibonacci function
#Exponential
def myfib2(val):
    if val <= 0: #Base case
        return 0
    if val <= 1: #Another base case
        return 1
    #Recursive case
    return myfib2(val-1) + myfib2(val-2)

#Print 10 fibonacci numbers
for index in range(11):
    print(str(myfib2(index)) + " "),