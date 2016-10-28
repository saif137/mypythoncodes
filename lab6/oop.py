#Class for faculty data
class faculty:
    name=""
    design=""
    dept=""
    id=""
    def __init__(self, name="", design="", dept="", id=""):
        self.name = name
        self.design = design
        self.dept = dept
        self.id = id

    def printdata(self):
        print("->Name>>"+self.name+"<-:->Desig>>"+self.design+"<-:->Dept>>"+self.dept+"<-:->ID>>"+self.id+"<-")

#Class for student data
class student:
    name=""
    regno=""
    batch=""
    program=""
    def __init__(self, name="", regno="", batch="", program=""):
        self.name = name
        self.regno = regno
        self.batch = batch
        self.program = program

    def printdata(self):
        print("|Name:"+self.name+"|Reg:"+self.regno+"|Batch:"+self.batch+"|Program:"+self.program+"|")

unidata = [
    faculty("name","design", "dept", "id"),
    student("name", "regno", "batch", "program"),
] #Empty list to store all data

def inputfaculty():
    global unidata
    obj = faculty()
    obj.name = raw_input("Enter faculty name")
    obj.id = raw_input("Enter faculty id")
    obj.design = raw_input("Enter faculty designation")
    obj.dept = raw_input("Enter faculty department")
    unidata.append(obj)


def inputstudent():
    global unidata
    obj = student()
    obj.name = raw_input("Enter student name")
    obj.regno = raw_input("Enter student reg no")
    obj.batch = raw_input("Enter student batch")
    obj.program = raw_input("Enter faculty program")
    unidata.append(obj)

def inputfunc():
    ip2 = raw_input("Press f for faculty data insertion \nor s for student data insertion \nor r to return to main menu")
    if ip2 == "f":
        inputfaculty()
    elif ip2 == "s":
        inputstudent()
    elif ip2 == "r":
        return
    else:
        print("Invalid choice")

def printfunc():
    global unidata
    for data in unidata:
            print(data.printdata())

if __name__ == "__main__":
    while True:
        print("Welcome menu:")
        print("Press i to insert")
        print("Press p to print")
        print("Press e to exit")
        ip = raw_input("Enter choice:")
        if ip.lower() == "e":
            exit()
        elif ip.lower() == "i":
            inputfunc()
        elif ip.lower() == "p":
            printfunc()
        else:
            print("Invalid choice")