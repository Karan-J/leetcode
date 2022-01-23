'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

https://leetcode.com/problems/linked-list-cycle-ii/

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head) -> ListNode:
        # O(n) space. very simple
#         visited = set()
#         temp = head
        
#         while temp is not None:
            
#             if temp in visited:
#                 return temp
#             else:
#                 visited.add(temp)
#                 temp = temp.next
                
#         return 

#         if head is None or head.next is None:
#             return 
    
    # O(1) space
    slow = head
    fast = head
    ptr2 = fast
    
    while not (fast is None or fast.next is None):
        
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    ptr2 = slow
    
    if fast is None or fast.next is None:
        return 
        
    ptr1 = head
    
    while ptr1 != ptr2:
        ptr2 = ptr2.next
        ptr1 = ptr1.next
    
    return ptr1

if __name__ == '__main__':
    head = ListNode(1)
    print(detectCycle(head))