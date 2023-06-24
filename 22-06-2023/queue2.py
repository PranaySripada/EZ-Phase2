queue=[]
def enqueue():
    element=int(input("Enter an element"))
    queue.append(element)
    print(element,"is added to q")
def dequeue():
    if not queue:
        print("q is empty")
    else:
        e=queue.pop(0)
        print("Removed Element:",e)
def display():
    print(queue)
while True:
    print("Select Operation 1.Add 2.Remove 3.Display 4.Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    else:
        break
