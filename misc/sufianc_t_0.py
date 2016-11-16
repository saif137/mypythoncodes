import math

#Task 0
def tht_power(a,b):
    d = 1
    while b != 0:
        if b%2 == 1:
            d = d * a
        a = a * a
        b = math.floor(b/2)
    return d
#TAsk 1
def digit_addition(n):
    s = 0
    a = n
    while a != 0:
        b = a % 10
        a = a // 10
        s = s + b
    return s

#Unsucessfull attempt without sort
def lda(n):
    a = n
    lsta = []
    while a != 0:
        b = a % 10
        a = a // 10
        lsta.append(b)
    print(lsta)

#Task 2

def nCr(n,r):
    f = math.factorial
    return f(n)/(f(r)*f(n-r))

def pascal(n):
    lsta = []
    for i in range(n+1):
        lsta.append(int(nCr(n,i)))
    return lsta
        
def aks_test(p):
    coefficient_list = pascal(p)
    for c in coefficient_list:
        if c % p != 0 and c != 1:
            print(c)
            return False
        elif c > 1:
            if coefficient_list[int(c)] == coefficient_list[int(c-1)]:
                break
    return True


