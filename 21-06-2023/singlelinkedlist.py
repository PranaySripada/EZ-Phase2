# LInked list
#creating node-declaration & defination
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
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

    def delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
               
    def delete_at_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range (1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def search(self,num):
        flag=0
        self.num=num
        temp=self.head
        while temp:
            if temp.data==num:
                flag=1
                break
            temp=temp.next
        if flag==1:
            print("Element found")
        else:
            print("Element Not found")

obj=singlelinkedlist()
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
while(1):
    print("---------------------------")
    print("Select an option:")
    print("1.Insert at Begining.")
    print("2.Insert at End.")
    print("3.Insert at Position.")
    print("4.Delete at Begining.")
    print("5.Delete at End.")
    print("6.Delete at Position.")
    print("7.Search")
    print("8.Display")
    A=int(input("Enter your choice:"))
    if A==1:
        ele=int(input("Enter an Element"))
        print("After Inserting",ele," at begining")
        obj.insert_begining(ele)
        obj.display()
    if A==2:
        ele=int(input("Enter an Element"))
        print("After Inserting",ele," at end")
        obj.insert_last(ele)
        obj.display()
    if A==3:
        ele=int(input("Enter an Element"))
        print("After Inserting",ele," at position")
        obj.insert_at_position(ele)
        obj.display()
    if A==4:
        obj.delete()
        obj.display()
    if A==5:
        obj.delete_at_end()
        obj.display()
    if A==6:
        pos=int(input("Enter a position"))
        obj.delete_position(pos)
        obj.display()
    if A==7:
        num=int(input("Enter a number to be searched"))
        obj.search(num)
    if A==8:
        obj.display()

    









