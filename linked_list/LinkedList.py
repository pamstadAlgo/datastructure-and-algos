
class Node:
    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def add(self, item):
        """
        adds an item to the head of the list. We need to differentiate the following case:

        1) LinkedList is empty and we add an item --> in this case size is 0; then this node becomes head and tail of linked list
        2) LinkedList is not yet empty --> set new item as head and link it to previous head
        """
        if self.size == 0:
            node = Node()
            node.data = item
            self.head = node
            self.tail = node
            self.size += 1
        else:
            #store current head in intermediate variable
            old_head = self.head

            #create new node that will be new head
            node = Node()
            node.data = item
            node.next = old_head

            #set new node as head
            self.head = node

            #increased linked list size
            self.size += 1

    def append(self, item):
        """
        appends an item to the end of the linked list. We need to differentiate two cases:

        1) LinkedList is empty --> in this case node because head and tail
        2) LinkedList is not empty --> new node becomes tail. Old tail node will point to new tail node
        """
        if self.size == 0:
            node = Node()
            node.data = item
            self.head = node
            self.tail = node
            self.size += 1
        else:
            #store old tail
            old_tail = self.tail

            #create new tail
            node = Node()
            node.data = item

            # set new tail
            self.tail = node

            # point old tail to new tail
            old_tail.next = node

            #increase size of linked list
            self.size += 1
    
    def pop(self, pos=None):
        """
        returns and last item in the list

        We need to cover the following cases:
        1) LinkedList is empty --> do we raise an error?
        2) if only one element --> set head and tail none
        3) more than one element in Linked List --> I think we need to traverse the linked list, no other way
        """

        # if linked list is empty inform about empty linked list
        if self.size == 0:
                print('Empty linked list')
                return None
        

        #pop last element
        if pos is None or pos == self.size -1:
            if self.size == 1:
                #return the head and set tail and head to None
                head = self.head
                self.head = None
                self.tail = None
                self.size -= 1
                return head
            
            current_node = self.head

            while current_node:
                next_node = current_node.next
                # get next node
                if next_node.next is None:
                    print(f'we break loop. Current_node: {current_node.data}, tail node: {next_node.data}')
                    break
                else:
                    current_node = next_node

            #when loop breaks we have found tail
            tail = self.tail

            # set node before tail as tail, which will be the current node
            self.tail = current_node
            current_node.next = None

            #reduce size
            self.size -= 1
            return tail
        else:
            """
            Pop element at certain position. We need to make sure that pos is within size; we assume zero index
            """
            if pos > self.size -1:
                print(f'no element at pos {pos}, size of linked list is only {self.size}')
                return Node()

            if self.size == 1:
                #return the head and set tail and head to None
                head = self.head
                self.head = None
                self.tail = None
                self.size -= 1
                return head
            
            # cover case where we pop head and linked list is bigger than 1
            if pos == 0:
                head = self.head
                node_after_head = head.next
                self.head = node_after_head
                self.size -= 1
                return head
            
            """
            case where we pop an element inbetween
            """
            node_pos = 0
            current_node = self.head

            while current_node:

                #check if we are at requested position
                if pos == node_pos:
                    #point previous node to next node
                    previous_node.next = current_node.next
                    self.size -= 1
                    return current_node
                else:
                    previous_node = current_node
                    current_node = current_node.next
                    node_pos += 1

    def search(self, item):
        """
        search for an item; return true if found, false otherwise
        """
        current_node = self.head
        while current_node:
            if current_node.data == item:
                return True
            
            current_node = current_node.next
        
        return False

    def remove(self,item):
        """
        removes an item
        """
        current_node = self.head
        while current_node:
            if current_node.data == item:
                #link previous node to next node
                previous_node.next = current_node.next
                break

            previous_node = current_node
            current_node = current_node.next
    


    def __str__(self):
        parts = []
        current = self.head
        while current:
            nxt = current.next.data if current.next else None
            parts.append(f"({current.data}, next={nxt})")
            current = current.next
        return " --> ".join(parts)
    


linked_list = LinkedList()

linked_list.add(12)
linked_list.add(23)

linked_list.append(111)

#print(linked_list)


linked_list.add(33)

linked_list.append(99)

linked_list.add(1)

print(linked_list)

search_item = 23

print(f'item {search_item} in linked_list: {linked_list.search(search_item)}' )

linked_list.remove(search_item)

print(linked_list)


print(f'item {search_item} in linked_list: {linked_list.search(search_item)}' )

#tail = linked_list.pop()

#we expect data 12
# popped_element = linked_list.pop(0)

# print(f'popped element: {popped_element.data}')

# print(linked_list)

