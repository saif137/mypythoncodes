'''
Iterative merge sort
Developer: Dr. Syed Saif ur Rahman
Purpose: Educational
'''
import math #We used log, ciel

#Merges the data to bring them in order
def merge(l1, l2, s):
    global mydata
    global mydatalen
    #print("merge " + str(l1) + " with " + str(l1 + s) + " for " + str(s) + " elements ")
    l = [None] * (s) #Temporary list to store left half of data
    r = [None] * (s) #Temporary list to store right half of data
    for index in range(s):
        if l1 + index < mydatalen: #check if index is valid
            l[index] = mydata[l1 + index]
        if l2 + index < mydatalen: #check if index is valid
            r[index] = mydata[l2 + index]

    #print("l " + str(l))
    #print("r " + str(r))
    i = 0
    j = 0
    for k in range (l1,l2+s):
        if k < mydatalen:
            if l[i] <= r[j] or r[j] is None: # None check for odd case
                mydata[k] = l[i]
                i = i + 1
                if i >= s :
                    while j < s :
                        k = k + 1
                        if k >= mydatalen:break;
                        mydata[k] = r[j]
                        j = j + 1
                    break;
            else:
                mydata[k] = r[j]
                j = j + 1
                if j >= s :
                    while i < s :
                        k = k + 1
                        if k >= mydatalen:break;
                        mydata[k] = l[i]
                        i = i + 1
                    break;

#Test data
#mydata = [9, 1, 8, 2, 7, 3, 6, 4, 5]
#mydata = [9, 1, 8, 2, 7, 3, 6, 4, 5,9, 1, 8, 2, 7, 3, 6, 4, 5]
#mydata = [9, 1, 8, 2, 7, 3, 6, 4, 5, 9, 1, 8, 2, 7, 3, 6, 4, 5, 9, 1, 8, 2, 7, 3, 6, 4, 5]
#mydata = [-1, 8, -2, 7, -3, 6, -4, 5]
#mydata = [9, -8, 2, 7, 3, 6, 4, 5, -9, 1, 8, 2, 7, 3, 6, 4, -5]
mydata = [9, 1, 8, 2, -3, 6, 4, 5, 9, 1, -8, 2, 7, 3, 6, 4, 5, 9, 1, 8, 2, 7, 3, 6, -4, 5]
mydatalen = len(mydata)
print("math.log(mydatalen, 2)", math.log(mydatalen, 2))
#Depth of imaginary tree
depth = int(math.ceil(math.log(mydatalen, 2)))
print("Tree depth", depth)
x = 0
for level in range(depth - 1,-1,-1):
    print("Tree level", level)
    sp = 2**level
    print("Sub problems", sp)
    #sps = mydatalen / 2**level #Cant figure out why it is wrong
    sps = 2 ** x
    print("Sub problem size", sps)
    print("mydata -> " + str(mydata))
    for mi in range(0,mydatalen,sps*2):
        merge(mi,mi+sps,sps)
        print("mydata -> " + str(mydata))
    x += 1