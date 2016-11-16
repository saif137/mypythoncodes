def printcalc(calvalues):
    for key in calvalues.keys():
        print "Key: " + str(key) + "Value: " + str(calvalues[key])


def mynaivebayeslearnpredict(mydata, mypredict):
    no_columns = len(mydata)
    print "no_columns = " + str(no_columns)
    no_rows = len(mydata[mydata.keys()[0]])
    print "no_rows = " + str(no_rows)
    from collections import defaultdict
    occurance_counts = defaultdict(float)
    prob_counts = defaultdict(float)
    for looper2 in range(0, no_columns - 1):
        label_counts = defaultdict(float)
        for looper1 in range(0, no_rows):
            occurkey = mydata.keys()[looper2] + ":" + mydata[mydata.keys()[looper2]][looper1] + " and " + \
                       mydata[mydata.keys()[no_columns - 1]][looper1]
            occurance_counts[occurkey] += 1
            label_counts[mydata[mydata.keys()[no_columns - 1]][looper1]] += 1
            probkey = mydata.keys()[looper2] + ":" + mydata[mydata.keys()[looper2]][looper1] + " given " + \
                      mydata[mydata.keys()[no_columns - 1]][looper1]
            prob_counts[probkey] = occurance_counts[occurkey] / label_counts[
                mydata[mydata.keys()[no_columns - 1]][looper1]]
    printcalc(prob_counts)

    predict_counts = defaultdict(float)
    for looper1 in range(0, no_columns - 1):
        precol = mypredict.keys()[looper1] + ":" + mypredict[mypredict.keys()[looper1]]
        for key in prob_counts.keys():
            col, label = key.split(" given ")
            if precol == col:
                # print precol
                # print prob_counts[key]
                predict_counts[label] += prob_counts[key]
    printcalc(predict_counts)
    winlab = 0.0
    label = ""
    for key in predict_counts.keys():
        if winlab < predict_counts[key]:
            label = key
            winlab = predict_counts[key]
    print "Prediction is : " + label

if __name__ == "__main__":
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
    predictval = {"temp": "low", "humid": "low", "outlook": "overcast", "windy": "false"}
    mynaivebayeslearnpredict(myweatherdict, predictval)
