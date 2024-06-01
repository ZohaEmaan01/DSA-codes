# linked nodes based code for implementation of TREE basics
class Tree:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.children = []

    def __init__(self):
        self.root = None

    class PreIterator:
        def __init__(self, node, tree):
            self.stk = [node]

        def __next__(self):
            if len(self.stk) > 0:
                cur = self.stk[-1]
                del self.stk[-1]
                for c in reversed(cur.children):
                    self.stk.append(c)
                return cur.data
            else:
                raise StopIteration

    def __iter__(self):
        return self.PreIterator(self.root, self)

    def addnode(self, n, p=None):
        if p == None and self.root == None:
            self.root = self.Node(n)
        elif p == None:
            raise Exception("Root aleady exist")
        elif n != None and p != None:
            if self.root.data == p:
                self.root.children.append(self.Node(n))
            else:
                self.addnodeAux(self.root, n, p)

    def addnodeAux(self, r, n, p):
        for c in r.children:
            if c.data == p:
                c.children.append(self.Node(n))
                return
            self.addnodeAux(c, n, p)

    def size(self):
        return self.sizeAux(self.root)

    def sizeAux(self, node):
        if node is None:
            return 0
        else:
            count = 1  # count the current node
            for child in node.children:
                count += self.sizeAux(child)  # recursively count the children
            return count

    def leaves(self):
        return self.leavesAux(self.root)

    def leavesAux(self, node):
        if node is None:
            return 0
        elif len(node.children) == 0:
            return 1  # node is a leaf
        else:
            count = 0
            for child in node.children:
                count += self.leavesAux(child)  # recursively count the leaves in each child node
            return count

    def update(self, o, n):
        node = self.searchAux(self.root, o)  # search for the node with data value o
        if node is None:
            raise Exception("Node with data value " + str(o) + " not found in tree")
        node.data = n  # update the data value of the node to n

    def searchAux(self, node, data):
        if node is None:
            return None
        elif node.data == data:
            return node
        else:
            for child in node.children:
                result = self.searchAux(child, data)
                if result is not None:
                    return result
            return None

    def depth(self, n):
        return self.depthAux(self.root, n, 0)

    def depthAux(self, r, n, depth):
        if r == None:
            return -1
        elif r.data == n:
            return depth
        else:
            for c in r.children:
                d = self.depthAux(c, n, depth + 1)
                if d != -1:
                    return d
            return -1

    def cut_paste(self, o, n):
        node, parent = self.find_node_and_parent(o)
        if node is None:
            return False
        parent.children.remove(node)
        self.addnode(node.data, n)
        return True

    def find_node_and_parent(self, data):
        node = self.root
        parent = None
        while node is not None:
            if node.data == data:
                return node, parent
            parent = node
            for child in node.children:
                node = child if child.data == data else None
                if node is not None:
                    return node, parent
        return None, None

    def remove(self, v):
        if self.root == None:
            return
        if self.root.data == v:
            self.root = None
            return
        self.removeAux(self.root, v)

    def removeAux(self, r, v):
        for c in r.children:
            if c.data == v:
                r.children.remove(c)
                return True
            else:
                if self.removeAux(c, v):
                    return True
        return False

    def Display(self):
        self.DisplayAux(self.root)
        print()

    def DisplayAux(self, r):
        if r != None:
            print(r.data)
            for c in r.children:
                self.DisplayAux(c)


def main():
    # Create a new tree
    t = Tree()
    # add the root element to the tree
    # add the element as child node to an existing node of tree
    t.addnode(10)
    t.addnode(30, 10)
    t.addnode(200, 10)
    t.addnode(70, 10)
    t.addnode(2, 30)
    t.addnode(50, 30)
    t.addnode(92, 200)
    t.addnode(60, 200)
    t.addnode(12, 70)
    t.addnode(2000, 60)
    t.addnode(7000, 60)
    t.addnode(55, 60)

    # Display tree data
    print("Display tree data")
    t.Display()

    print()

    print("OUTPUT of 'for d in t:'")
    for d in t:
        print(d)
    print()

    print("Size of the tree:", t.size())
    print()

    print("Number of leaves in the tree:", t.leaves())
    print()

    print("Depth of node with data 10:", t.depth(10))  # Depth should be 0
    print("Depth of node with data 30:", t.depth(30))  # Depth should be 1
    print("Depth of node with data 2000:", t.depth(2000))  # Depth should be 3
    print("Depth of node with data 50:", t.depth(50))  # Depth should be 2
    print()

    t.update(30, 40)
    print("Display updated tree data")
    t.Display()
    print()

    t.cut_paste(200, 55)
    print("Display tree data after cut_paste operation")
    t.Display()

    t.remove(2000)
    print("Display tree data after removing subtree with node data 2000")
    t.Display()

main()
