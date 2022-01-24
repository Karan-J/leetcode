'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB) -> [ListNode]:
    
    setA = set()
    tempA = headA
    while tempA is not None:
        setA.add(tempA)
        tempA = tempA.next
    
    tempB = headB
    while tempB is not None:
        if tempB in setA:
            return tempB
        tempB = tempB.next
        
    return 

if __name__ == '__main__':
    headA = ListNode(1)
    headA.next = ListNode(3)
    headB = ListNode(3)
    print(getIntersectionNode(headA,headB))