#Implementation of Binary Search Using Recursive

#My own implementaion using pseudo code
#It works if vdatal is in data list
#Note this implementation matches Pseudo Code

def binsrch(vdatal,data,left,right):
    #"""vdatal = value to search"""
    m = (left+right)//2
    if vdatal == data[m]:
        return True
    if vdatal < data[m]:
        return binsrch(vdatal,data,left,m-1)
    else:
        return binsrch(vdatal,data,m+1,right)

LIST = [1,2,3,4,5,6,7,8,9,10]

print(binsrch(6,LIST,0,len(LIST)-1))

#Crashes due to infinite recursion
#print(binsrch(11,LIST,0,len(LIST)-1))


#Code you provided
#Error : mydata is not

def binary_search(val, lowerBound, upperBound):
    current = (lowerBound + upperBound) / 2
    if LIST[current] == val:
        print("Data found at: ", current)
        return
    elif upperBound < lowerBound:
        print("Data not found")
        return
    else:
        if LIST[current] > val:
            return binary_search(val, lowerBound, current - 1)
        elif LIST[current] < val:
            return binary_search(val, current + 1, upperBound)

def call_binary_search(val, mydata):
    binary_search(val, 0, len(mydata) - 1)

call_binary_search(9, LIST)
