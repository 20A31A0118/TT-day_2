class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head =new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    def show(self):
        if self.head is None:
             print("Stack list is empty")
        else:
             p=self.head
             while p is not None:
                 print(p.data)
                 p=p.next


                 
a_stack = Stack()
while True:
    print('1) Push')
    print('2) Pop')
    print('3) Exit')
    print('4) Display')

    do = input('What would you like to do?')

    #operation = do [00].strip().lower()
    operation = do
    if operation == '1':
        a_stack.push (int(input("Enter the value:")))
    elif operation == '2':
        if popped is None:
            print('Stack is empty.')
        else:
            print('popped value :', int(popped))
    elif operation == '3':
        break
    elif operation == '4':
        a_stack.show()
        
        
        
