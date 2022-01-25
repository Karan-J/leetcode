'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2
Input: head = [1,2]
Output: [2,1]

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(head):
    if head is None or head.next is None:
        return head

    curHead = head
    
    while head.next is not None:
        p = head.next
        head.next = p.next
        p.next = curHead
        curHead = p

    return curHead

def printLinkedList(head):
    li = []
    temp = head
    while temp:
        li.append(temp.val)
        temp = temp.next
    print(li)

if __name__ == '__main__':
    headA = ListNode(1)
    headA.next = ListNode(3)
    printLinkedList(headA)
    reverseLinkedList(headA)
    printLinkedList(headA)
