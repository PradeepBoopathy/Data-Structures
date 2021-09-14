class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self,data):
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
        if self.head is None:
            return 0
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            print('Invalid Index')
            return
        if index == 0:
            self.insert_at_beg(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                cur = itr.next
                itr.next = Node(data, cur)
            count += 1
            itr = itr.next

    def remove_at(self, index):
        if index == 0:
            cur = self.head.next
            self.head = cur
            return
        if index < 0 or index > self.get_length():
            print('Invalid Index')
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                cur = itr.next.next
                itr.next = cur
                break
            count += 1
            itr = itr.next

    def insert_after_values(self, data_insert, after_data):
        itr = self.head
        while itr:
            if after_data == itr.data:
                cur = itr.next
                node = Node(data_insert, cur)
                itr.next = node
            itr = itr.next

    def print(self):
        if self.head is None:
            print('Empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    data = [1, 2, 3, 4, 5]
    ll.insert_values(data)
    print(ll.get_length())
    #ll.insert_at(2, 2.5)
    ll.remove_at(2)
    ll.insert_after_values(4.5, 4)
    ll.print()