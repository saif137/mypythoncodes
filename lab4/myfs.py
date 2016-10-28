import os

searchpath = "C:\Python27"
mydatafile = open("mysysfiles.csv", "w+")

if os.path.isdir(searchpath):  # if this is a directory,
    for filename in os.listdir(searchpath):  # then for each child:
        childpath = os.path.join(searchpath, filename)  # compose full path to child
        if not os.path.isdir(childpath):
            #print("filename: " + filename)
            mydata = filename + ", " + childpath + "\n"
            mydatafile.write(mydata)
        else:
            for filenamec in os.listdir(childpath):  # then for each child:
                childpathc = os.path.join(childpath, filenamec)  # compose full path to child
                if not os.path.isdir(childpathc):
                    # print("filename: " + filename)
                    mydata = filenamec + ", " + childpathc + "\n"
                    mydatafile.write(mydata)
                else:
                    for filenamecc in os.listdir(childpathc):  # then for each child:
                        childpathcc = os.path.join(childpathc, filenamecc)  # compose full path to child
                        if not os.path.isdir(childpathcc):
                            # print("filename: " + filename)
                            mydata = filenamecc + ", " + childpathcc + "\n"
                            mydatafile.write(mydata)

mydatafile.close()