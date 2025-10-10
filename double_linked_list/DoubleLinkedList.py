
class Node:
    def __init__(self, data=None, prev = None, _next=None):
        self.data = data
        self.next = _next
        self.prev = prev

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    

    def add(self,item):
        """
        Adds new node at the head of the linked list
        when adding we cover the cases where:
        1) linked list still empty
        2) linked list has nodes (so head already exists)
        """
        if self.size == 0:
            node = Node()
            node.data = item
            node.prev = None
            node.next = None
            self.head = node
            self.tail = node
            self.size += 1
        else:
            #get old head
            old_head = self.head

            #create new head
            node = Node()
            node.data = item
            node.prev = None
            node.next = old_head

            #set new head
            self.head = node
            old_head.prev = node

            #increase size
            self.size += 1

    def append(self, item):
        """
        adds an item at the end of the list. We differentiate the following cases
        1) linked list is empty --> then it is same as add
        2) linked list is not empty --> case treated separately
        """
        if self.size == 0:
            self.add(item)
        else:
            #get current tail
            tail = self.tail

            #create new node
            node = Node()
            node.data = item
            node.prev = tail
            node.next = None

            #set next of previous tail to new tail
            tail.next = node

            #set new tail
            self.tail = node

            #increase size of linked list
            self.size += 1

    def pop(self, pos=None):
        """
        Removes nodes from given position. If pos is None, last node will be removed
        """
        if pos is None or pos == self.size - 1:
            #get tail
            tail = self.tail

            #get previous node which will be new tail
            new_tail = tail.prev
            new_tail.next = None
            self.tail = new_tail

            #decrease size
            self.size -= 1



    def __str__(self):
        parts = []
        current = self.head
        while current:
            prev_data = current.prev.data if current.prev else None
            next_data = current.next.data if current.next else None
            parts.append(f"({prev_data} <- {current.data} -> {next_data})")
            current = current.next
        return " <=> ".join(parts)



dll = DoubleLinkedList()


dll.add(12)

dll.add(32)



dll.append(100)

#print(dll)


dll.add(99)

dll.add(1)

#print(dll)

dll.append(55)


print(dll)


dll.pop()

print(dll)

dll.pop()

print(dll)