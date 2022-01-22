'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1   // -4 points to 2
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head) -> bool:
    # iterative solution
    if head is None:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        
        slow = slow.next
        fast = fast.next.next
        
    return True

    # recursive solution
    # if not head:
    #     return False
    # return cycle(head,head.next)
    
def cycle(n1,n2):
    if n1 == n2:
        return True
    if n2 is None or n2.next is None:
        return False
    return cycle(n1.next,n2.next.next)

if __name__ == '__main__':
    head = ListNode(1)
    print(hasCycle(head))