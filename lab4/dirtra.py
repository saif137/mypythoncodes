import os

mydatafile = open("lpsassignstdata.csv", "w+")

'''Return the number of bytes used by a file / folder and any descendents.'''
def diskusage(path):
    global mydatafile
    if os.path.isdir(path):  # if this is a directory,
        for filename in os.listdir(path):  # then for each child:
            childpath = os.path.join(path, filename)  # compose full path to child
            if childpath.__contains__('.git') or childpath.__contains__('.DS_Store'):
                continue
            #print("childpath:" + childpath)
            if not os.path.isdir(childpath):
                #print("filename: " + filename)
                #print("path:" + path)
                flist=path.split("\\")
                lenflist = len(flist)
                mydata = ""
                if lenflist > 1:
                    #print("studentid:"),
                    print(flist[1]+","+filename),
                    mydata  += flist[1]+","+filename
                    if filename.__contains__(".tex"):
                        print(",Latex file submitted"),
                        mydata += ",Latex file submitted"
                    else:
                        print(","),
                        mydata += ","
                    if lenflist > 2:
                        print(",created folders"),
                        mydata += ",created folders"
                    else:
                        print(","),
                        mydata += ","
                    if filename.__contains__(".pdf"):
                        print(",PDF file submitted"),
                        mydata += ",PDF file submitted"
                    else:
                        print(","),
                        mydata += ","
                    if filename.__contains__(".zip"):
                        print(",zip file submitted"),
                        mydata += ",zip file submitted"
                    else:
                        print(","),
                        mydata += ","
                    if filename.__contains__(".rar"):
                        print(",rar file submitted"),
                        mydata += ",rar file submitted"
                    else:
                        print(","),
                        mydata += ","
                    print("") #For new line
                    mydata += "\n"
                    mydatafile.write(mydata)
                #print("studentid:"),
                #print(flist)
            diskusage(childpath) #Add child usage to total

def A():
    afile = open("IDsA.txt","r")
    dfile = open("lpsassignstdata.csv","r")
    for aline in afile:
        found = 0
        if aline.strip() == 'aa02190':
            print(aline)
        for dline in dfile:
            print(dline.split(","))
            if aline.strip() == dline.split(",")[0] and (found == 0 or found == 1):
                print(dline),
                found = 1
            elif found == 1:
                dfile.seek(0)
                break;
        if found == 0:
            print(aline.strip()+",No submission on GIT"),
        print("")
    afile.close()
    dfile.close()

if __name__ == '__main__':
    #diskusage("C:/lpsassignments/")
    A()
    mydatafile.close()