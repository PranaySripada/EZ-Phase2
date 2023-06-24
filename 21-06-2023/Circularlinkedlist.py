# LInked list
#creating node-declaration & defination
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circularlinkedlist:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_last(self,data):
        nl=Node(data)
        curr=self.head
        if curr==None:
            print("Linked list is empty")
        else:
            
            while curr.next:
                curr=curr.next
            curr.next=nl
    def insert_at_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head#temo=first node
            while temp.next  :
                print(temp.data,end="-> ")
                #temp.data means first node's data
                temp=temp.next#establishing link
            print(temp.data)

obj=circularlinkedlist()
#node creation-initialising
n=Node(10)# so n.data in Node class will be 10
obj.head=n# assigning first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
n6=Node(70)
n5.next=n
obj.display()









