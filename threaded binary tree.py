class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.leftThread = False
        self.rightThread = False

class ThreadedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None
        while current:
            parent = current
            if data < current.data:
                if current.leftThread:
                    break
                current = current.left
            else:
                if current.rightThread:
                    break
                current = current.right

        if data < parent.data:
            new_node.left = parent.left
            new_node.right = parent
            parent.leftThread = False
            parent.left = new_node
        else:
            new_node.left = parent
            new_node.right = parent.right
            parent.rightThread = False
            parent.right = new_node

    def in_order_traversal(self):
        current = self._leftmost(self.root)
        while current:
            print(current.data, end=" ")
            if current.rightThread:
                current = current.right
            else:
                current = self._leftmost(current.right)
        print()

    def pre_order_traversal(self):
        current = self.root
        while current:
            print(current.data, end=" ")
            if not current.leftThread:
                current = current.left
            elif not current.rightThread:
                current = current.right
            else:
                while current and current.rightThread:
                    current = current.right
                if current:
                    current = current.right
        print()

    def _leftmost(self, node):
        while node and not node.leftThread:
            node = node.left
        return node

# Example Usage
if __name__ == "__main__":
    tree = ThreadedBinaryTree()
    tree.insert(20)
    tree.insert(10)
    tree.insert(30)
    tree.insert(5)
    tree.insert(15)
    tree.insert(25)
    tree.insert(35)

    print("In-order traversal: ", end="")
    tree.in_order_traversal()

    print("Pre-order traversal: ", end="")
    tree.pre_order_traversal()
