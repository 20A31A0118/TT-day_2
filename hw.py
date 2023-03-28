class Node:
    count=0
    def __init__(self, data):
        self.left = None
        self.right =None
        self.data = data
    def insert(self,data):
        if self.data:
            if data < self.data:
                self.count=self.count+1
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                #data > self.data
                self.count=self.count+1
                if self.right is None:
                    #self.count=self.count+2
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def findval(self, lkpval):
      if lkpval < self.data:
        if self.left is None:
          return str(lkpval)+ " Not Found"
        return self.left.findval(lkpval)
      elif(lkpval > self.data):
        if self.right is None:
            return str(lkpval)+"Not Found"
        return self.right.findval(lkpval)
      else:
          return str(str(self.data) + ' is found ')
            
    def PrintTree(self):
        if self.left:
             self.left.PrintTree()
        print(self.data)
        if self.right:
           self.right.PrintTree()
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))
print(root.count+1)
            

            
                
                    
