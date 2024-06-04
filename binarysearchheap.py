class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if node.left:
                self._insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._insert(val, node.right)
            else:
                node.right = Node(val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        elif val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                temp = self._find_min(node.right)
                node.val = temp.val
                node.right = self._delete(node.right, temp.val)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(node.val)
            self._print_tree(node.right)

    def search(self, val):
        return self._search(val, self.root)

    def _search(self, val, node):
        if not node:
            return False
        elif val == node.val:
            return True
        elif val < node.val:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)

def main():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print("Before deletion:")
    bst.print_tree()

    print("Searching for 4:", bst.search(4))
    print("Searching for 10:", bst.search(10))

    bst.delete(3)
    bst.delete(8)

    print("After deletion:")
    bst.print_tree()
    print("Searching for 3:", bst.search(3))
    print("Searching for 8:", bst.search(8))
    print("Searching for 2:", bst.search(2))
main()
