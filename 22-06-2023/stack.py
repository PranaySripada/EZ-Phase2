#Stack
stack=[]
def push():
    element=int(input("Enter the element"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)
def top_element():
    if not stack:
        print("No Top Element(Stack is empty)")
    else:
        print("Top Element=",stack[-1])
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
        print(stack)
    elif choice==5:
        print("Okay Bye")
        break
