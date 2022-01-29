'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRight(head,k):
    if head is None or head.next is None:
        return head

    size = 1
    original_tail = head
    while original_tail.next is not None:
        original_tail = original_tail.next
        size += 1

    original_tail.next = head 
    new_tail = head

    for i in range( size - (k % size) - 1 ):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


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
    headA.next.next = ListNode(2)
    printLinkedList(headA)
    headB = rotateRight(headA,4)
    printLinkedList(headB)