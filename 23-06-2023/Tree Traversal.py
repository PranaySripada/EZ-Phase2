class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def printInorder(root):
    if root:
        #first recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end=" ")
        #now recur on right child
        printInorder(root.right)

def printPostorder(root):
    if root:
        #first recur on the left child
        printPostorder(root.left)
        #now recur on right child
        printPostorder(root.right)
        # then print the data of node
        print(root.val,end=" ")
        


def printPreorder(root):
    if root:
        #first print the data of node
        print(root.val,end=" ")
        #then recur on the left child
        printPreorder(root.left)
        #finally recur on right child
        printPreorder(root.right)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("PRE-ORDER")
printPreorder(root)
print("\nIN-ORDER")
printInorder(root)
print("\nPOST-ORDER")
printPostorder(root)







