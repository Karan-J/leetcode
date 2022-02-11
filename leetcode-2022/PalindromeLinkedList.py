'''
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

'''

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def isPalindrome(head):
    l = []
    temp = head
    while temp is not None:
        l.append(temp.val)
        temp = temp.next
    print(l)
    return l == l[::-1]

if __name__ == '__main__':
    h = ListNode(1)
    e = ListNode(2)
    l = ListNode(2)
    o = ListNode(1)
    h.next = e
    e.next = l
    l.next = o
    print(isPalindrome(h))
    e.next = None
    print(isPalindrome(h))