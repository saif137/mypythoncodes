class mynode:
    data = ""
    left = None
    right = None

class mytree:
    head = None
    def insert(self, data):
        if self.head == None:
            self.head = mynode()
            self.head.data = data
        else:
            tmp = mynode()
            tmp.data = data
            curr = self.head
            while True:
                if tmp.data < curr.data :
                    if curr.left == None:
                        curr.left = tmp
                        break #Done with insert
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = tmp
                        break #Done with insert
                    else:
                        curr = curr.right

    def search(self, data):
        tmp = self.head
        while True:
            if tmp == None:
                print("Element not found")
                break # Record not found and we are at empty leaf
            elif tmp.data == data:
                print("Element found")
                break #We have found record
            else:
                if data < tmp.data:
                    tmp = tmp.left
                else:
                    tmp = tmp.right

    def preorder(self,node):
        if node == None:
            return
        print(node.data),
        print(" "),
        self.preorder(node.left)
        self.preorder(node.right)

    def preordertraverse(self):
        self.preorder(self.head)

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data),
        print(" "),
        self.inorder(node.right)

    def inordertraverse(self):
        self.inorder(self.head)

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data),
        print(" "),

    def postordertraverse(self):
        self.postorder(self.head)


if __name__ == "__main__":
    obj = mytree()
    obj.insert("one")
    obj.insert("two")
    obj.search("two")
    obj.search("three")
    obj.insert("zero")
    obj.insert("three")
    obj.insert("four")
    obj.insert("seven")
    obj.insert("six")
    obj.insert("five")
    obj.search("six")
    print("Preorder: "),
    obj.preordertraverse()
    print("\nInorder: "),
    obj.inordertraverse()
    print("\nPostorder: "),
    obj.postordertraverse()
    print("")

    obj1 = mytree()
    obj1.insert("1")
    obj1.insert("2")
    obj1.search("2")
    obj1.search("3")
    obj1.insert("0")
    obj1.insert("3")
    obj1.insert("4")
    obj1.insert("7")
    obj1.insert("6")
    obj1.insert("5")
    obj1.search("6")
    print("Preorder: "),
    obj1.preordertraverse()
    print("\nInorder: "),
    obj1.inordertraverse()
    print("\nPostorder: "),
    obj1.postordertraverse()
