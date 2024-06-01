# linked nodes based code for implementation of LIST basics
class doublyLinkedList:
    class Node:
        def __init__(self,data=None):
            self.data=data
            self.next=None
            self.prev=None

    class DLLIterator:
        def __init__(self, node, list):
            self.current = node
            self.list = list
        def __eq__( self, rhs ):
            return self.current == rhs.current
        def __ne__( self, rhs ):
            return self.current != rhs.current
        def getObject( self ):
            return self.current.data
        def __iter__(self):  # this is not mandatory, why
            return self
        def __next__( self ):
            if self.current.next != self.list.tail:
                cur_node = self.current
                self.current = self.current.next
                return self
            else:
                raise StopIteration

    class DLLRIterator:
        def __init__(self, node, list):
            self.current = node
            self.list = list
        def __eq__( self, rhs ):
            return self.current == rhs.current
        def __ne__( self, rhs ):
            return self.current != rhs.current
        def getObject( self ):
            return self.current.data
        def __iter__(self):  # this is mandatory, why
            return self
        def __next__( self ):
            if self.current.prev != self.list.head:
                cur_node = self.current
                self.current = self.current.prev
                return self
            else:
                raise StopIteration

    def __init__(self):
        self.head=self.Node()
        self.tail=self.Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def __iter__(self):
        return self.DLLIterator(self.head, self)

    def __reversed__(self):
        return self.DLLRIterator(self.tail, self)

    def begining(self):
        return self.DLLIterator(self.head, self)

    def end(self):
        return self.DLLIterator(self.tail.prev, self)

    def rbegining(self):
        return self.DLLRIterator(self.tail, self)

    def rend(self):
        return self.DLLRIterator(self.head.next, self)





    def append(self,o):
        t=self.Node(o)
        t.next=self.tail
        t.prev=self.tail.prev
        self.tail.prev.next=t
        self.tail.prev=t

    def remove(self, index):
        cur = None
        if type(index) is int:
            cur=self.head.next
            i=0
            while i!=index and cur!=self.tail:
                i=i+1
                cur=cur.next
            if cur==self.tail:
                raise Exception
        elif type(index) is self.DLLIterator:
            cur = index.current
        cur.prev.next=cur.next
        cur.next.prev=cur.prev
        del cur

    def search(self,val):
        cur = self.head.next
        while cur!=self.tail:
            if cur.data == val:
                return True
            cur = cur.next
        return False

    def set(self,old,new):
        cur = self.head.next
        while cur!= self.tail:
            if cur.data == old:
                cur.data = new
            else:
                cur = cur.next

    def clone(self):
        dll1 = doublyLinkedList()
        cur = self.head.next
        while cur!= self.tail:
            dll1.append(cur.data)
            cur = cur.next
        return dll1

    def same(self,dll1):
        cur = self.head.next
        cur1 = dll1.head.next
        while cur!=self.tail and cur1!=self.tail:
            if cur.data == cur1.data:
                return True
            else:
                cur = cur.next
                cur1 = cur1.next
        return False

    def Display(self):
        cur=self.head.next
        while cur!=self.tail:
            print(cur.data, end=" ")
            cur=cur.next
        print()

def main():
    # Create a new Doubly Linked List
    dll = doublyLinkedList()
    # Insert the element to empty list
    dll.append(10)
    # Insert the element at the end
    dll.append(20)
    dll.append(30)
    dll.append(70)
    dll.append(50)
    dll.append(60)
    dll.append(80)
    dll.append(90)
    dll.append(40)
    # Display Data
    print("Display 10 items")
    dll.Display()
    # Delete elements from start
    dll.remove(0)
    # Delete elements from end
    dll.remove(0)
    # Display Data
    print("Display without (removed) first two items")
    dll.Display()
    print()

    print("OUTPUT of 'for d in dll:'")
    for d in dll:
        print(d.getObject())
    print()

    print("OUTPUT of 'for d in reversed(dll):'")
    for d in reversed(dll):
        print(d.getObject())
    print()

    print("OUTPUT through manual next calls")
    itm1 = iter(dll)
    itm2 = dll.begining()

    print("first through itm1: " + str(next(itm1).getObject()))
    print("next  through itm1: " + str(next(itm1).getObject()))
    print("first through itm2: " + str(next(itm2).getObject()))
    print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm1: " + str(next(itm1).getObject()))
    print("Removing current data")
    dll.remove(itm1)
    print("Removed")
    print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm2: " + str(next(itm2).getObject()))
    # due to remove above, print("next  through itm2: " + str(next(itm2).getObject()))
    print("next  through itm1: " + str(next(itm1).getObject()))

    print()

    print("OUTPUT through beginning and end")
    i = dll.begining()
    while i != dll.end():
        i = next(i)
        print(i.getObject())
    print()

    print("OUTPUT through rbeginning and rend")
    i = dll.rbegining()
    while i != dll.rend():
        t = next(i)
        print(t.getObject())
    print()

    print("OUTPUT through rbeginning and rend")
    i = dll.rbegining()
    while i != dll.rend():
        t = next(i)
        print(t.getObject())
    print(dll.search(80))
    dll.set(70,4)
    dll.Display()
    dll1 = dll.clone()
    dll.Display()
    print(dll.same(dll1))
main()

