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

    def insert(self, node, index):
        i = 0
        current = self.head
        while(i != index):
            i += 1
            current = current.next
        current.next = node
            
    def delete(self, value):
        pass

    def contains(self, value):
        pass

