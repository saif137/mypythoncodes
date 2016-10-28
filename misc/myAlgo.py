from math import sin, pi

class mySortAlgo:

    @staticmethod
    def mergeSort(data):
        step = 1
        while step <= len(data):
            for index in range(0, len(data), step):
                print(index)
            step += 1
            print("\n")
        print("Data after iterative merge sort: " + str(data))

class mymath:

    @staticmethod
    def plotsin():
        loop1 = 0.0
        while loop1 <= 2:
            #print(round(sin(pi*loop1), 1) * 10)
            loop2 = 0
            while loop2 < (round(sin(pi*loop1), 1) * 10) + 10:
                loop2 += 1
                if abs(loop2) == 10:
                    print("|"),
                else:
                    if loop1 == 0.5:
                        print("-"),
                    else:
                        print(" "),
            print("*")
            loop1 += 0.1

class mydivconq:

    @staticmethod
    def multiply():
        var1 = 22222222222222222222222222222222222222222222222222222
        var2 = 33333333333333333333333333333333333333333333333333333
        print(var1 * var2)