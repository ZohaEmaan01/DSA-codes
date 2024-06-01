class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

    def addFrontNode(lnkNodes, val):
    tmp = Node(val,lnkNodes)
    lnkNodes = tmp
    return tmp

    def printLinkedNodes(lnkNodes):
    cn = lnkNodes
    while cn != None:
        print(cn.data, end=" ")
        cn = cn.link

    def addBackNode(lnkNodes, val):
    tmp = Node(val)
    cn = lnkNodes
    while cn.link != None:
        cn = cn.link
    cn.link = tmp

    # unable to add first node, how can we manage it	
    def removeNode(lnkNodes, val):
    cn = lnkNodes
    while cn.link != None:
        if cn.link.data == val:
            tmp = cn.link
            cn.link = tmp.link
            del tmp
        cn = cn.link

    def main():
    nodeSet1 = Node(125)
    printLinkedNodes(nodeSet1)
    print()
    nodeSet2 = Node(34)
    printLinkedNodes(nodeSet2)
    print()
    addBackNode(nodeSet2, 43)
    printLinkedNodes(nodeSet2)
    print()
    addBackNode(nodeSet2, 61)
    addBackNode(nodeSet2, 32)
    addBackNode(nodeSet2, 93)
    addBackNode(nodeSet1, 526)
    printLinkedNodes(nodeSet1)
    print()
    printLinkedNodes(nodeSet2)
    print()
    removeNode(nodeSet2,61)
    printLinkedNodes(nodeSet2)
    print()
    addFrontNode(nodeSet2, -7)
    printLinkedNodes(nodeSet2)
    print()
    # Following code is approimately as that of addFrontNode
    tmp = Node(-2)   # why working
    tmp.link = nodeSet2
    nodeSet2 = tmp
    #--------
    printLinkedNodes(nodeSet2)
    print()
    printLinkedNodes(nodeSet1)
    print()

    main()

