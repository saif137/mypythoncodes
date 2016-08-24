class mySearchAlgo:

    @staticmethod
    def linearSearchManual1(data, element):
        for delement in data:
            if delement == element:
                print("Element " + str(element) + " found at: " + str(data.index(element)))

    @staticmethod
    def linearSearchManual2(data, element):
        for index in range(len(data)):
            if data[index] == element:
                print("Element " + str(element) + " found at: " + str(index))

    @staticmethod
    def linearSearchAuto(data, element):
         print("Element " + str(element) + " found at: " + str(data.index(element)))

class mySortAlgo:

    @staticmethod
    def bubbleSort(data):
        for index1 in range (len(data) - 1):
            for index2 in range(index1, len(data)):
                if data[index1] > data[index2]:
                    temp = data[index1]
                    data[index1] = data[index2]
                    data[index2] = temp
        print("Data after bubble sort: " + str(data))

    @staticmethod
    def autoSort(data):
        data.sort()
        print("Data after default sort: " + str(data))