class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head, None)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, None, itr)
        itr.next = node

    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            print('Invalid Index')
            return

        if index == 0:
            self.insert_at_beg(data)
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
            count += 1
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print('Invalid Index')
            return
        if index == 0:
            itr = self.head
            self.head = itr.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                cur = itr.next.next
                cur.prev = itr
                itr.next = cur
            count += 1
            itr = itr.next

    def insert_after_value(self, data_insert, data_after):
        if self.head is None:
            print('Empty Linked List')
            return
        count=0
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count+1, data_insert)
                break
            itr = itr.next
            count += 1

    def remove_after_value(self,data_to_remove,data_after):
        if self.head is None:
            print('Empty LinkedList')
            return

        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                self.remove_at(count+1)
            count += 1
            itr = itr.next

    def print_forward(self):
        if self.head is None:
            print('Empty Linked List')
            return

        itr = self.head
        forward = ''
        while itr:
            forward += str(itr.data) + '--->'
            itr = itr.next
        print(forward)

    def get_lastnode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print('Empty List')
            return
        itr = self.get_lastnode()
        backward = ''
        while itr:
            backward += str(itr.data) + '<---'
            itr = itr.prev
        print(backward)

    def print(self):
        if self.head is None:
            print('Empty List')
            return

        itr = self.head
        dlstr = ''
        while itr:
            dlstr += str(itr.data) + '<-->'
            itr = itr.next
        print(dlstr)

if __name__ == '__main__':
    dl = DoublyLinkedList()
    datalist = [1, 2, 3, 4, 6, 7, 8, 9]
    dl.insert_values(datalist)
    dl.print_forward()
    dl.print_backward()
    dl.insert_at(4,5)
    dl.print_forward()
    dl.print_backward()
    dl.remove_at(0)
    dl.print_forward()
    dl.insert_after_value(4.5,4)
    dl.print_backward()
    dl.print_forward()
    dl.remove_after_value(3,2)
    dl.print_forward()
    #dl.print()
    #dl.print_forward()
    #dl.print_backward()