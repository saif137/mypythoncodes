##Name:Yasir Salim
# ID:Ys01840


##Welocm to my code
##here I am  searching file using binary search.
##I was unable to find the path of python that's why I used other path.

import math
import os

##This is what I searched, searchpath ="Windows C:\Users:\AppData:\Local:\Programs:\Python:\Python35-32"
searchpath = "C:\Python27"


def dir_search(searchpath):  ##This function is giving all files in path.
    mydatafile = open("mysysfiles.csv", "a")
    if os.path.isdir(searchpath):  # True if searchpath is directory
        for filename in os.listdir(searchpath):  # Creates a list with directory of files
            childpath = os.path.join(searchpath, filename)
            if not os.path.isdir(childpath):
                mydata = filename + "," + childpath + "\n"
                mydatafile.write(mydata)
            else:  # i think this should work..
                dir_search(childpath)
    mydatafile.close()


dir_search(searchpath)


def Over():
    mydatafile = open("mysysfiles.csv", "w")  ##here w means to overwrite everythinh
    dir_search("C:\Python27")
    mydatafile.close()


def merge(x, y):  ##using merge sort
    if x is None:
        return (y)
    k = len(x)
    if y is None:
        return (x)
    l = len(y)

    if k == 0:
        return (y)
    if l == 0:
        return (x)

    if x[0] <= y[0]:
        i = merge(x[1:], y)
        i.insert(0, x[0])
        return i
    else:
        j = merge(x, y[1:])
        j.insert(0, y[0])
        return j


def mergesort(a):
    n = len(a)
    if n > 1:
        k = merge(mergesort(a[0:len(a) // 2]), mergesort(a[len(a) // 2:]))
        return k
    else:
        return a


def lis(P_file):  ##here I am adding line is list and and creeating a list with user input.
    global LIST
    global f_list
    File = open("mysysfiles.csv", "r")
    for i in File:
        LIST.append(i.strip())
    File.close()

    LIST = mergesort(LIST)
    for e in LIST:
        T_V = e[:len(P_file)]
        f_list.append(T_V)
    return


def binary_search(val, low, high):  ##Binary search
    """
    Binary search function.
    Assumes 'items' is a sorted list.
    The search range is [low, high)
    """
    current = (low + high) // 2
    global file_list
    cur_val = f_list[current]
    cur_val = str(cur_val)
    if cur_val == val:
        return (True, current)
    elif high < low:
        return (False, 0)
    else:
        if cur_val > val:
            return binary_search(val, low, current - 1)
        elif cur_val < val:
            return binary_search(val, current + 1, high)


def c_b_s(val):  ##This is my main binary search function.
    global f_list
    T = binary_search(val, 0, len(f_list) - 1)
    return T


def main():  ##This function have every
    global LIST
    global f_list
    LIST = []
    f_list = []

    Over()
    print("Welcome for searching file")
    print("Search any file from path. It will help you to find path to that file")
    print("***************************")
    file = input("please write file directory:")
    lis(file)
    Binary = c_b_s(file)
    output = Binary[0]
    if output == True:
        print("Hurrah!,file found")
        e_dir = LIST[Binary[1]]
        e_dir = e_dir[len(file) + 2:]
        print("file directory" + e_dir)
    if output == False:
        print("File not found")


main()
