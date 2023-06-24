stack=[]
e=[]
flag=0
a=str(input())
x=len(a)
b=a[0:x//2]
c=a[x//2:x+1]
for i in b:
    stack.append(i)
print(stack)
def para(l):
    if '(' and ')' in l:
        flag=1
    elif '[' and ']' in l:
        flag=1
    elif '{' and '}' in l:
        flag=1
    return flag   
for i in range (x//2):
    e.append(stack.pop())
    l=c[i]+e[i]
    para(l)
if flag ==1:
    print("True")
else:
    print("False")

    
