class Node:
    def __init__(self, value, next_node=None, prev=None):
        self.value = value
        self.next = next_node
        self.prev = prev

    def __str__(self):
        return '{}'.format(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, head):
        self.head = head

    def set_tail(self, tail):
        self.tail = tail

    def add(self, node):
        self.tail.next = node    
        self.set_tail(node)

    def insert(self, node, index):
        i = 0
        prev = self.head
        current = self.head.next
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            while(i != index):
                i += 1
                prev = current
                current = current.next
        prev.next = node
        node.next = current
            
    def delete(self, value):
        pass

    def contains(self, value):
        pass
    
    def print_list(self):
        current = self.head
        while(current is not None):
            print(current)
            current = current.next

def reverse(head):
    current = head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def print_list_from_node(head):
    current = head
    while current:
        print(current.value)
        current = current.next

node1 = Node(1)
node2 = Node(2)
linkedList = LinkedList()
linkedList.set_head(node1)
linkedList.set_tail(node1)
linkedList.add(node2)
linkedList.print_list()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
rev = reverse(node1)
print_list_from_node(rev)
