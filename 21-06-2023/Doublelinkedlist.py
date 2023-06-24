#doubleLinkedList

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=' ')
                temp=temp.next
    def insert_at_begining(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head.previous=newnode
        self.head=newnode

    def insert_at_end(self,data):
        newnode=Node(data)
        temp=self.head

        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.previous=temp

    def insert_at_position(self,pos,data):
        newnode=Node(data)
        temp=self.head
        for i in range (pos-1):
            temp=temp.next
        newnode.previous=temp
        newnode.next=temp.next
        temp.next.previous=newnode
        temp.next=newnode

    def delete_at_begining(self):
        temp=self.head
        self.head=temp.next

    def delete_at_end(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.previous.next=None
        temp.previous=None

    def delete_at_position(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next.previous=temp.previous
        temp.previous.next=temp.next

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.insert_at_begining(50)
l.insert_at_end(400)
pos=int(input("Enter the position:"))
l.insert_at_position(pos,25)
l.display()
'''l.delete_at_begining()
l.delete_at_end()'''
pos=int(input("Enter the position:"))
l.delete_at_position(pos)
l.display()
