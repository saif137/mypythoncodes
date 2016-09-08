# Recursive mergesort using pseudocode from algorithms by Dasgupta et al.
import math

def merge(x,y):
    if x is None:return (y);
    k=len(x)
    if y is None:return (x)
    l=len(y)

    if k==0:return (y)
    if l==0:return (x)

    if x[0]<=y[0]:i = merge(x[1:],y);i.insert(0, x[0]);return i
    else:j = merge(x,y[1:]);j.insert(0, y[0]);return j

def mergesort(a):
    n=len(a)
    if n>1:k =  merge(mergesort(a[0:len(a)//2]), mergesort(a[len(a)//2:]));return k
    else:return a

if __name__ == "__main__":
    b = [9, 1, 8, 2, 7, 3, 6, 4, 5, 9, 1, 8, 2, 7, 3, 6, 4, 5, 9, 1, 8, 2, 7, 3, 6, 4, 5]
    c = [9, 1, 8, 2, -3, 6, 4, 5, 9, 1, -8, 2, 7, 3, 6, 4, 5, 9, 1, 8, 2, 7, 3, 6, -4, 5]
    myres1 = mergesort(b);print(myres1)
    myres2 = mergesort(c);print(myres2)