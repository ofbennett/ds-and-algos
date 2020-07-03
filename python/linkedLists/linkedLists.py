class SinglyLinkedList:
    class _Node:
        def __init__(self, item):
            self.item = item
            self.next = None
    
    def __init__(self, init_array = None):
        self.head = None
        if init_array:
            for item in reversed(init_array):
                self.push_head(item)

    def push_head(self,item):
        node = self._Node(item)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def push_tail(self,item):
        tail = self._get_tail_node()
        node = self._Node(item)
        if tail is None:
            self.head = node
        else:
            tail.next = node

    def pop_head(self):
        if self.head is None:
            return None
        old_head = self.head
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
        return old_head.item

    def pop_tail(self):
        if self.head is None:
            return None
        if self.head.next is None:
            old_head = self.head
            self.head = None
            return old_head.item
        length = self.get_length()
        current = self.head
        for _ in range(length-2):
            current = current.next
        new_tail = current
        old_tail = current.next
        new_tail.next = None
        return old_tail.item

    def get_length(self):
        node = self.head
        n = 0
        while node is not None:
            node = node.next
            n += 1
        return n

    def _get_tail_node(self):
        if self.head is None:
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        return current
    
    def _get_node_at(self, index):
        # Does not do "in bounds" checks. Do these in the calling function.
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def get_head(self):
        if self.head is None:
            return None
        else:
            return self.head.item
    
    def get_tail(self):
        if self.head is None:
            return None
        else:
            return self._get_tail_node().item
    
    def item_at(self,index):
        length = self.get_length()
        if index >= length or index < 0:
            raise IndexError(f"Index of {index} out of range in list of length {length}")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.item
    
    def get_list(self):
        l = []
        current = self.head
        while current is not None:
            l.append(current.item)
            current = current.next
        return l

    def delete_at(self, index):
        length = self.get_length()
        if index >= length or index < 0:
            raise IndexError(f"Index of {index} out of range in list of length {length}")
        if index == 0:
            old_head = self.head
            self.head = self.head.next
            del old_head
        else:
            node_before = self._get_node_at(index - 1)
            node_to_del = self._get_node_at(index)
            if index == length - 1:
                node_after = None
            else:
                node_after = self._get_node_at(index + 1)
            node_before.next = node_after
            del node_to_del

    def insert_at(self, item, index):
        # Inserts an item at specific index. The item at that index is pushed towards the tail (its index increases by one).
        length = self.get_length()
        if index >= length or index < 0:
            raise IndexError(f"Index of {index} out of range in list of length {length}")
        node = self._Node(item)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            node_before = self._get_node_at(index - 1)
            node_at_index = self._get_node_at(index)
            node_before.next = node
            node.next = node_at_index

    def reverse(self):
        if self.get_length() in [0,1]:
            return
        node1 = self.head
        node2 = self.head.next
        self.head.next = None
        while node2.next is not None:
            node3 = node2.next
            node2.next = node1
            node1 = node2
            node2 = node3
        node2.next = node1
        self.head = node2

class DoublyLinkedList:
    class _Node:
        def __init__(self, item):
            self.item = item
            self.next = None
            self.prev = None
    
    def __init__(self, init_array = None):
        self.head = None
        self.tail = None
        if init_array:
            for item in reversed(init_array):
                self.push_head(item)
    
    def push_head(self,item):
        node = self._Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        
    def push_tail(self,item):
        node = self._Node(item)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def pop_head(self):
        if self.head is None:
            return None
        old_head = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        return old_head
    
    def pop_tail(self):
        if self.tail is None:
            return None
        old_tail = self.tail
        if self.tail.prev is None:
            self.tail = None
            self.head = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return old_tail
    
    def get_head(self):
        if self.head is None:
            return None
        else:
            return self.head.item
    
    def get_tail(self):
        if self.tail is None:
            return None
        else:
            return self.tail.item
    
    def get_length(self):
        node = self.head
        n = 0
        while node is not None:
            node = node.next
            n += 1
        return n
    
    def get_list(self):
        l = []
        current = self.head
        while current is not None:
            l.append(current.item)
            current = current.next
        return l
    
    def item_at(self,index):
        length = self.get_length()
        if index >= length or index < 0:
            raise IndexError(f"Index of {index} out of range in list of length {length}")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.item
    
    def _get_node_at(self, index):
        # Does not do "in bounds" checks. Do these in the calling function.
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def delete_at(self, index):
        length = self.get_length()
        if index >= length or index < 0:
            raise IndexError(f"Index of {index} out of range in list of length {length}")
        if length == 1 and index == 0:
            single_item = self.head
            self.head = None
            self.tail = None
            del single_item
        elif index == 0:
            old_head = self.head
            self.head = self.head.next
            self.head.prev = None
            del old_head
        elif index == (length - 1):
            old_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del old_tail
        else:
            node_before = self._get_node_at(index - 1)
            node_to_del = self._get_node_at(index)
            node_after = self._get_node_at(index + 1)
            node_before.next = node_after
            node_after.prev = node_before
            del node_to_del

    def insert_at(self, item, index):
        # Inserts an item at specific index. The item at that index is pushed towards the tail (its index increases by one).
        length = self.get_length()
        if index >= length or index < 0:
            raise IndexError(f"Index of {index} out of range in list of length {length}")
        node = self._Node(item)
        if length == 1 and index == 0:
            item_at_index = self.head
            self.head = node
            self.head.next = item_at_index
            self.tail = item_at_index
            self.tail.prev = node
        elif index == 0:
            old_head = self.head
            self.head = node
            self.head.next = old_head
            old_head.prev = self.head
        else:
            node_before = self._get_node_at(index - 1)
            node_at_index = self._get_node_at(index)
            node_before.next = node
            node.next = node_at_index
            node.prev = node_before
            node_at_index.prev = node
    
    def reverse(self):
        if self.get_length() in [0,1]:
            return
        node1 = self.head
        self.tail = node1
        node2 = self.head.next
        self.head.next = None
        self.head.prev = node2
        while node2.next is not None:
            node3 = node2.next
            node2.next = node1
            node2.prev = node3
            node1 = node2
            node2 = node3
        node2.next = node1
        node2.prev = None
        self.head = node2
    
    def _is_all_connected(self):
        # Debugging function that checks all necessary links exits within the list
        if self.head is None and self.tail is None:
            return
        current = self.head
        while current.next is not None:
            current = current.next
        assert(current is self.tail)
        while current.prev is not None:
            current = current.prev
        assert(current is self.head)
        