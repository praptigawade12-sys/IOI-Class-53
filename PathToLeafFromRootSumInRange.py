class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def pathsum(r,s):
    if not r:
        return False

    if not r.left and not r.right:
        return r.data == s

    return pathsum(r.left,s-r.data) or pathsum(r.right,s-r.data)

r = Node(5)
r.left = Node(4)
r.right = Node(8)
r.left.left = Node(11)
r.left.left.left = Node(7)
r.left.left.right = Node(2)
r.right.left = Node(13)
r.right.right = Node(4)

print(pathsum(r,26))
print(pathsum(r,22))
print(pathsum(r,18))