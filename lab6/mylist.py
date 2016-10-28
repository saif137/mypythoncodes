class mynode:
    data = ""
    next = None

class mylist:
    head = None
    def insert(self, data=""):
        if self.head == None:
            self.head = mynode()
            self.head.data = data
        else:
            tmp = mynode()
            tmp.data = data
            tmp.next = self.head
            self.head = tmp

    def printlist(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next

if __name__ == "__main__":
    obj = mylist()
    obj.insert("one")
    obj.insert("two")
    obj.printlist()
    obj.insert("zero")
    obj.printlist()