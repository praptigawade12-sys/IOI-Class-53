from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printKdistace(r,target,k):
    q = deque([r])
    target_node = None
    parent = {}

    while q:
        node = q.popleft()

        if node.data == target:
            target_node = node

        if node.left:
            parent[node.left] = node
            q.append(node.left)

        if node.right:
            parent[node.right] = node
            q.append(node.right)

    q = deque([(target_node,0)])
    visited = {target_node}

    while q:
        node , d = q.popleft()

        if d == k:
            print(node.data, end = " ")
            continue

        for x in (node.left, node.right, parent.get(node)):
            if x and x not in visited:
                visited.add(x)
                q.append((x, d+1))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printKdistace(root,2,1)