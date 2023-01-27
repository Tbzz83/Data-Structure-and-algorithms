# This showcases a single linked-list, and has some added useful functionality
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        # Both Head and next are nodes. Starting with one data point, it initially writes the
        # Node as a data point, next = None
        # it then assigns the Head value to this node you just created

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        # If there is nothing in the list, set your new data point as this node

        itr = self.head
        while itr.next:
            itr = itr.next
        # While there is a next available node (itr.next exists), keep iterating until you get to a node that
        # Doesn't have a next node
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        # Simple counting how many elements
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        if self.head.data == data:
            self.head = itr.next
            return

        while itr:
            if itr.next is None:
                print("The value " + data + " is not in list")
                break
            if itr.next.data == data:
                itr.next = itr.next.next
                break


            itr = itr.next






if __name__ == '__main__':
    ll = linked_list()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
