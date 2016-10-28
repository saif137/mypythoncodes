import random, time

#Use system clock to feed as seed to random function
random.seed(time.clock)
#Number of elements
count = 0
#Total elements
tele = 15
#Tuple with list of dates
dates = ("31 Oct","2 Nov", "4 Nov", "4 Nov", "4 Nov",
         "7 Nov", "9 Nov", "11 Nov", "11 Nov", "11 Nov",
         "14 Nov", "16 Nov", "18 Nov", "18 Nov", "18 Nov")
#List to store numbers
data = []
while True:
    #Generate a random number
    val = random.randrange(1, tele + 1)
    found = 0
    #Check if number is already used
    for dval in data:
        if dval == val:
            found = 1
            break
    #Add new random number to list
    if found == 0:
        data.append(val)
        count = count + 1
        if count == tele:
            break;
#Print both tuples and list
for i in range(tele):
    print("Date: " + str(dates[i]) + " -> Group: " + str(data[i]))