'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1,l2):
    dummy = ListNode(0)
    cur = dummy
    s = 0
    carry = 0
    p1 = l1
    p2 = l2

    while p1 is not None or p2 is not None:
        x = p1.val if p1 is not None else 0
        y = p2.val if p2 is not None else 0
        s = x + y + carry 
        carry = s // 10
        cur.next = ListNode(s % 10)
        cur = cur.next
        if p1 is not None:
            p1 = p1.next
        if p2 is not None:
            p2 = p2.next

    if carry > 0:
        cur.next = ListNode(carry)

    return dummy.next


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
    headB = ListNode(2)
    headB.next = ListNode(9)
    s = addTwoNumbers(headA,headB)
    printLinkedList(s)

    