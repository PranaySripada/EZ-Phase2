class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head = self.head.next
            return popped

    def display(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            temp=self.head
            while temp.next:
                print(temp.data,end="-->")
                temp=temp.next
            print(temp.data)
obj=stack()

while True:
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Quit")
    choice=int(input("Enter your choice"))
    if choice==1:
        element=int(input("Enter Element to be inserted"))
        obj.push(element)
    elif choice==2:
        obj.pop()
    elif choice==3:
        obj.display()
    else:
        print("GOOD BYE")
        break

