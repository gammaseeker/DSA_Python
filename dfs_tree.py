class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def dfs_tree(root):
  if root.left:
    dfs_tree(root.left)
  if root.right:
    dfs_tree(root.right)
  print(root.val)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node5
node2.right = node6
dfs_tree(node1)

