from sklearn.naive_bayes import GaussianNB

mycsv = open("weather.csv")
myweatherdict = {}
temp = []
humid = []
outlook = []
windy = []
label = []
count = 0
for line in mycsv:
    if (count != 0):
        tempt, humidt, outlookt, windyt, labelt = line.split(",")
        temp.append(tempt)
        humid.append(humidt)
        outlook.append(outlookt)
        windy.append(windyt)
        label.append(labelt)
    else:
        count += 1

myweatherdict["temp"] = temp
myweatherdict["humid"] = humid
myweatherdict["outlook"] = outlook
myweatherdict["windy"] = windy
myweatherdict["label"] = label

# fit a Naive Bayes model to the data
model = GaussianNB()
model.fit(myweatherdict[3], myweatherdict[4])
print(model)
# make predictions
#predicted = model.predict(testframe)
#print(predicted)