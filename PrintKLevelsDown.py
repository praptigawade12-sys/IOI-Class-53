class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printk(root,k):
    if root is None:
        return

    if k == 0:
        print(root.data, end = " ")
    else:
        printk(root.left,k-1)
        printk(root.right,k-1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

k = 2
printk(root,k)
print()