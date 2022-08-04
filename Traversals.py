# Tree traversels 

#Tree structure
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

#Preorder Traversal
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

#Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

#Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


#Intsertion data in tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)

