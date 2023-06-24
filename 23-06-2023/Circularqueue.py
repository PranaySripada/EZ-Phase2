class CircularQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        if ((self.rear+1)%self.size==self.front):
            print("Queue is full")
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            #always add element at rear place
        else:
            #next position or rear
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data

    def dequeue(self):
        if (self.front==-1):
            #condition for empty queue
            print("Queue is Empty")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        #condition for empty queue
        if (self.front==-1):
            print("Queue is Empty")
        elif (self.rear>=self.front):
            print("Elements in the circular queue",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("Elements",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
        if((self.rear+1)%self.size==self.front):
            print("Queue is full")
obj=CircularQueue(5)
obj.enqueue(5)
obj.enqueue(10)
obj.enqueue(15)
obj.enqueue(20)
obj.display()
print("Deleted Value=",obj.dequeue())
print("Deleted Value=",obj.dequeue())
obj.display()
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(50)
obj.display()
#it won't be inserted because Queue is full
obj.enqueue(69)

