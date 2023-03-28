class Node:
    def __init__(self, key):
        self.left = None
        self.right =None
        self.val = key

    def traversePreOrder(self):
        print(self.val, end= '')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()


    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end= '')    
        if self.right:
            self.right.traverseInOrder()


    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end= '')    



root = Node('apple')

root.left = Node('banana')
root.right = Node(2)

root.left.left = Node(" ")
root.left.right = Node('z')
'''root.right.left = Node('f')
root.right.right = Node('g')
root.left.right.left = Node('h')
root.right.left.right = Node('j')
root.right.right.right =Node('k')'''

print("Pre order Traversal:", end="")
root.traversePreOrder()
print("\nIn order Traversal:", end="")
root.traverseInOrder()
print("\nPost order Traversal:", end="")
root.traversePostOrder()
              
            
