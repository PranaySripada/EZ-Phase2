#Distributing Even and Odd Numbers into different stacks and implementing stack operations.
stack=[]
even=[]
odd=[]
def push():
    size=int(input("Enter the size of Stack"))
    for i in range (size):
        element=int(input("Enter The Element"))
        if element%2==0:
            even.append(element)
        else:
            odd.append(element)
def pop_element():
    a=int(input("1 or 2"))
    if a==1:
        if not even:
            print("Stack is empty")
        else:
            e=even.pop()
            print("Removed element:",e)
            print(even)
    elif a==2:
        if not odd:
            print("Stack is empty")
        else:
            e=odd.pop()
            print("Removed element:",e)
            print(odd)
def top_element():
    a=int(input("1 or 2"))
    if a==1:
        if not even:
            print("No Top Element(Stack is empty)")
        else:
            print("Top Element=",even[-1])
    elif a==2:
        if not odd:
            print("No Top Element(Stack is empty)")
        else:
            print("Top Element=",odd[-1])

def display():
    a=int(input("1 or 2"))
    if a==1:
        print(even)
    elif a==2:
        print(odd)
    
while True:
    print("Select operation 1.Push 2.Pop 3.Top/Peak 4.Display 5.Quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        top_element()
    elif choice==4:
        display()
    elif choice==5:
        print("Okay Bye")
        break
