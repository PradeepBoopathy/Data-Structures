class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self,datalist):
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

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            print('Invalid Index')
            return

        if index == 0:
            itr = self.head
            self.head = itr.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            count += 1
            itr = itr.next

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            print('Invalid Index')
            return

        if index == 0:
            self.insert_at_beg(data)

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
            count += 1
            itr = itr.next

    def remove_by_value(self, data):
        if self.head.data == data:
            itr = self.head
            self.head = itr.next

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                cur = itr.next.next
                itr.next = cur
                break
            itr = itr.next

    def insert_after_value(self, data_before, data_insert):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_before:
                cur = itr.next
                node = Node(data_insert, cur)
                itr.next = node
            itr = itr.next

    def print(self):
        if self.head is None:
            print('Linkedlist is empty')
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    datalist = [10, 20, 30, 40, 50]
    ll.insert_values(datalist)
    ll.insert_at(5,0)
    ll.insert_at(15, 2)
    ll.insert_at(25, 4)
    ll.insert_at(35, 6)
    ll.insert_at(45, 8)
    ll.insert_at(55, 10)
    ll.remove_by_value(25)
    ll.insert_after_value(5,6)
    ll.insert_after_value(20,25)
    print(ll.get_length())
    ll.print()