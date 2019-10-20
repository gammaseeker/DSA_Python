class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

#1->2->3->4->null

def reverse(head):
    current = head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

head = reverse(node1)
current = head
while current:
    print(current.value)
    current = current.next

