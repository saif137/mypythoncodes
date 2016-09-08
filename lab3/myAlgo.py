'''
Selection sort example
Developer: Dr. Syed Saif ur Rahman
Purpose: Educational
'''

from math import sin, pi

class mySortAlgo:

    #Selection sort example
    @staticmethod
    def selectionSort(data):
        for index1 in range (len(data) - 1):
            min = index1;
            for index2 in range(index1 + 1, len(data)):
                if data[index2] < data[min]:
                    min = index2;
            temp = data[index1]
            data[index1] = data[min]
            data[min] = temp
        print("Data after selection sort: " + str(data))

#Using selection sort
mySortAlgo.selectionSort([5, 3, 1, 4, 2])