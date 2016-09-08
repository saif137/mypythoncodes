'''
Iterative and recursive binary search implementations
Developer: Dr. Syed Saif ur Rahman
Purpose: Educational
'''

# Test data for search
mydata = [-2, -1, 0,1,2,3,4,5,6,7,8,9,10,11,12,13]
#mydata = [13,12,11,10,9,8,7,6,5,4,3,2,1]

#Iterative binary search
def binarysearchi(val):
    global mydata
    startindex = searchindex = 0
    searchspace = len(mydata)
    while True:
        #Search from mid point in search space of data
        searchindex = searchspace/2
        cval = mydata[startindex + searchindex]
        if val == cval:print("Data found at index :", startindex + searchindex);return
        else:
            if val > cval:startindex = searchindex + 1
        #Shrink the search space to half
        searchspace = searchspace / 2
        #searchspace is consumed or start crossed the end
        if startindex > len(mydata) or searchspace == 0:
            break #Data not found

def binarysearchri(val, lowerBound, upperBound):
    current = (lowerBound + upperBound) / 2
    if mydata[current] == val :print("Data found at: ", current);return;
    elif upperBound < lowerBound:print("Data not found");return;
    else:
        if mydata[current] > val:
            return binarysearchri(val, lowerBound, current - 1)
        elif mydata[current] < val:
            return binarysearchri(val, current + 1, upperBound)

#Recursive binary search
def binarysearchr(val):
    binarysearchri(val, 0, len(mydata) - 1)

#Testing iterative binary search
binarysearchi(3)
#Testing recursive binary search
#binarysearchr(7)
#binarysearchr(11)