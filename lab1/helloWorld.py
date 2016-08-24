#! C:\Python27
from myAlgo import mySearchAlgo, mySortAlgo

def say_hello(name):
    """say_hello: string -> .
    Consumes: a string, name
    Produces: nothing
    Purpose: prints a greeting of the form "Hello <name>!"
    """
    print "Hello " + name + "!" #this is the function body

if __name__ == "__main__":
    say_hello("Computational Thinking II")
    mySearchAlgo.linearSearchManual1([3, 5, 1, 7], 5)
    mySearchAlgo.linearSearchManual2([3, 5, 1, 7], 5)
    mySearchAlgo.linearSearchAuto([3, 5, 1, 7], 5)
    mySortAlgo.bubbleSort([3, 5, 1, 7])
    mySortAlgo.autoSort([3, 5, 1, 7])
