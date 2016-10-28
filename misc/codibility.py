val1 = 553
#Temp list to hold values
val1list = []
#Loop to separate values
while val1 > 0:
    print(val1 - (val1/10)*10)
    val1list.append(val1 - (val1/10)*10)
    val1 = val1/10
#Sort the values to get the largest number
val1list.sort(reverse=True)
#Just checking if it is correct
print(val1list)
#initiating the result with LSB
result = val1list[len(val1list) - 1]
#To increase the power to make integer again
power = 10
#Generating result
for num in range(len(val1list) - 2,-1,-1):
    result = result + val1list[num] * power
    power = power * 10
print(result)