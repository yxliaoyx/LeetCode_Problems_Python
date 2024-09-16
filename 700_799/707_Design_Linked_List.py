class MyLinkedList:
    def __init__(self):
        self.linkedlist = []

    def get(self, index: int) -> int:
        return self.linkedlist[index] if 0 <= index < len(self.linkedlist) else -1

    def addAtHead(self, val: int) -> None:
        self.linkedlist.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.linkedlist.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index <= len(self.linkedlist):
            self.linkedlist.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.linkedlist):
            self.linkedlist.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
