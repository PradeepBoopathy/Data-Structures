class Binarysearchtree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def insert(self, data):
        if self.data == data:
            return
        if self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Binarysearchtree(data)
        if self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Binarysearchtree(data)

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def preorder_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()
        elements.append(self.data)
        return elements

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    def levelorder_traversal(self):
        elements = []
        elements.append([self.data])
        thislevel = [self]
        nextlevel = []
        while len(thislevel) != 0:
            temp = []
            for x in thislevel:
                if x.left:
                    temp.append(x.left.data)
                    nextlevel.append(x.left)
                if x.right:
                    temp.append(x.right.data)
                    nextlevel.append(x.right)
            elements.append(temp)
            thislevel = nextlevel
            nextlevel = []
        return elements[:-1]

    def max_depth(self):
        if self.data is None:
            return 0
        return len(self.levelorder_traversal())

    def search(self, val):
        if self.data == val:
            return True
        if self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if self.data < val:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = Binarysearchtree(elements[0])
    for i in range(1, len(elements)):
        root.insert(elements[i])

    return root

if __name__ == '__main__':
    element = [17, 12, 2, 4, 6, 13, 15, 22, 21]
    number_tree = build_tree(element)

    print('Pre-Order Traversal', number_tree.preorder_traversal())
    print('Post-Order Traversal', number_tree.postorder_traversal())
    print('In-Order Traversal', number_tree.inorder_traversal())
    print('level-Order Traversal', number_tree.levelorder_traversal())
    print('Search value present in tree', number_tree.search(20))
    print('Minimum value in a tree', number_tree.find_min())
    print('Maximum value in a tree', number_tree.find_max())
    print('Maximum depth of a tree', number_tree.max_depth())