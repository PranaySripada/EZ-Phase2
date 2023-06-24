class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=self.head
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
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
                print(temp.data,end="<--")
                temp=temp.next
            print(temp.data)
obj=queue()

while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Quit")
    choice=int(input("Enter your choice"))
    if choice==1:
        element=int(input("Enter Element to be inserted"))
        obj.enqueue(element)
    elif choice==2:
        obj.dequeue()
    elif choice==3:
        obj.display()
    else:
        print("GOOD BYE")
        break
