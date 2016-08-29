#! C:\Python27
#Importing our classes
from myAlgo import mySearchAlgo, mySortAlgo
from myAlgoNoop import linearSearchManual1, linearSearchManual2, linearSearchAuto, bubbleSort, autoSort

#Checking if every thing is working
def say_hello(name):
    """say_hello: string -> .
    Consumes: a string, name
    Produces: nothing
    Purpose: prints a greeting of the form "Hello <name>!"
    """
    print "Hello " + name + "!" #this is the function body

#To keep track of where it all started
if __name__ == "__main__":
    say_hello("Computational Thinking II OOPS based implementation")
    mySearchAlgo.linearSearchManual1([3, 5, 1, 7], 5)
    mySearchAlgo.linearSearchManual1((3, 5, 1, 7), 5)
    mySearchAlgo.linearSearchManual2([3, 5, 1, 7], 5)
    mySearchAlgo.linearSearchManual2((3, 5, 1, 7), 5)
    mySearchAlgo.linearSearchAuto([3, 5, 1, 7], 5)
    mySearchAlgo.linearSearchAuto((3, 5, 1, 7), 5)
    mySortAlgo.bubbleSort([3, 5, 1, 7])
    mySortAlgo.insertionSort([3, 5, 1, 7])
    mySortAlgo.selectionSort([3, 5, 1, 7])
    mySortAlgo.autoSort([3, 5, 1, 7])

    say_hello("Computational Thinking II NOOPS based implementation")
    linearSearchManual1([3, 5, 1, 7], 5)
    linearSearchManual1((3, 5, 1, 7), 5)
    linearSearchManual2([3, 5, 1, 7], 5)
    linearSearchManual2((3, 5, 1, 7), 5)
    linearSearchAuto([3, 5, 1, 7], 5)
    linearSearchAuto((3, 5, 1, 7), 5)
    bubbleSort([3, 5, 1, 7])
    autoSort([3, 5, 1, 7])