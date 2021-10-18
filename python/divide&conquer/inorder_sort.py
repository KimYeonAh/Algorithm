import random

class TNode :
    def __init__ (self, data, left, right) :
        self.data = data
        self.left = left
        self.right = right

def newTree(n, m) :
    if m.data > n.data :
        if m.left is not None :
            newTree(n, m.left)
        else :
            m.left = n
    else :
        if m.right is not None :
            newTree(n, m.right)
        else :
            m.right = n

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end = ' ')
        inorder(n.right)

tree = [0]*20
tree[0] = TNode(random.randrange(0, 1000), None, None)

for i in range(1, 20) :
    tree[i] = TNode(random.randrange(0, 1000), None, None)
    newTree(tree[i], tree[0])

inorder(tree[0])
