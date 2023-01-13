class Node:
    """Creates a node to store/pass in data into LinkedList class."""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        """Utility function to print function calls."""
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            # linkedlist str itr can use ".data" because itr is the node object that was set as the head
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_beginning(self, data):
        # Creates a node and sets it as the head
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        """Create a new node at the end of the last node."""
        if self.head is None:
            # 2nd parameter is None because node is being inserted at the end
            # meaning node.next is null
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next: # keeps going until there is not more itr.next
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            self.head = Node(data_to_insert, None)
            return

        itr = self.head
        for itr in range(self.get_length()):
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr.itr.next

    def remove_at(self, index):
        # Ensures given index is valid within the linkedlist
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        # Checks if index being removed is the head.
        # if so, remove current head and assign next node as new head
        if index == 0:
            self.head = self.head.next
            return

        # For linkedlist you need to manually maintain a count to reach the desired index
        # this is because we need to know teh indexes of the element we are removing & the element prior to
        count = 0
        itr = self.head


        while itr:
            if count == index - 1: # we need to stop at the element before the element we are removing
                # itr.next is what remove by assigning it to itr.next.next (i.e.the element AFTER the one we removed)
                itr.next = itr.next.next
                break

            itr = itr.next  # works in while loop to go through each element in linkedlist
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



if __name__ == '__main__':
    # ll = LinkedList()
    # ll.insert_values(["banana", "mango", "grapes", "orange"])
    # print(ll.get_length())
    # ll.insert_at(3, "blueberry")
    # # ll.remove_at(2)
    # ll.print()
    #
    # ll.insert_values([45, 7, 12, 567, 99])
    # ll.insert_at_end(67)
    # ll.print()

    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    # ll.remove_by_value("orange")  # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()



# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list_exercise.md
