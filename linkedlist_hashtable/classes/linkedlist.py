#!python
from classes.node import Node

class Linkedlist(object):
    def __init__(self, items=None):
        """Initialise this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        node_counter = 0 
        for item in self.items():
            node_counter += 1
        return node_counter

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)
        # First we check if we have any nodes to begin with.
        if self.is_empty():
            # If self.head is None, it means there are no nodes in self
            # this means the new_node will both represent both the head 
            # and the tail.
            self.head = new_node
            self.tail = new_node

        # The first node that is appended is the head, the last is the tail. 
        # The 'head' is the first first node, the 'tail' is the last node. 
        else:
            # Point tail to new_node.
            self.tail.next = new_node
            self.tail = new_node
            
    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        # TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        # TODO: Best case running time: O(???) Why and under what conditions?
        # TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        # * Quality is a function that will be used to find the boolean value of
        # * a condition. For example, if "the" is in our linked list, it will 
        # * return true. This allows our quality function to be abstracted/generic.

        if self.is_empty():
            print("{} is not in linkedlist".format(quality))
            return None
        else:
            current_node = self.head
            # Quality function is used to see if conditions are met.
            for i in range(0, self.length()):
                if quality(current_node.data):
                    return current_node.data
                else:
                    # Iterating through linkedlist, continues unitil "quality" is found.
                    current_node = current_node.next
            return current_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        # TODO: Best case running time: O(???) Why and under what conditions?
        # TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        if self.is_empty():
            print("Linkedlist is completley empty")
            return
        
        current_node = self.head 
        previous_node = None
        
        while current_node:
            # * Loop through all nodes in linkedlist until 
            # * current_node.data is equal to the passed-in argument item.
            if current_node.data != item:
                previous_node = current_node
                current_node = current_node.next
            else:
                # * If a match is found, check if its the head node. 
                if self.head == current_node:
                    # Deleting the next of the current_node. 
                    current_node.next = None
                    return
                # *If match is found, check if its the tail node. 
                if self.tail == current_node:
                    # Deleting the next of the previous_node so the current_node is deleted.
                    previous_node.next = None
                    return
                # * If match is found, check if it is neither the head or 
                # * tail node. This means it just needs to skill the 
                # * current_node to delete it. 
                else:
                    previous_node.next = current_node.next
                    return 
            raise ValueError('Item not found: {}'.format(item))

              

        
    




