class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 
        temp = self.head
        i = 0
        while i <= index:
            temp = temp.next
            i += 1
        return temp.val

    
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index < 0:
            index = 0  
        self.size += 1
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
            
        cur = Node(val)
        cur.next = temp.next
        temp.next = cur
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        
        self.size -= 1
        prev = self.head
        for _ in range(index):
            prev = prev.next
            
        prev.next = prev.next.next

    
class Node:
    
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(0)
obj.addAtHead(1)
obj.addAtTail(2)
obj.addAtIndex(1,3)
# obj.deleteAtIndex(index)
obj.addAtHead(7)
obj.addAtTail(8)
# w = obj.get(1)

for i in range(obj.size):
    print(obj.get(i))

def printLinkedList(head):
    li = []
    temp = head
    while temp:
        li.append(temp.val)
        temp = temp.next
    print(li)

# printLinkedList(obj)




# class MyLinkedList:

#     def __init__(self):
#         self.head = Node()
#         self.ind = 0

#     def get(self, index: int) -> int:
#         temp = self.head
#         while self.ind != index:
#             temp = temp.next
#         return temp.val

#     def addAtHead(self, val: int) -> None:
#         cur = Node(val)
#         cur.next = self.head.next
#         self.head = cur

#     def addAtTail(self, val: int) -> None:
#         cur = Node(val)
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
#         temp.next = cur
#         cur.next = None

#     def addAtIndex(self, index: int, val: int) -> None:
        
#         pass

#     def deleteAtIndex(self, index: int) -> None:
#         pass

    
# class Node:
    
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
        
