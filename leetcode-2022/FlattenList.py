'''
You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

Example 1:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]

Example 3:
Input: head = []
Output: []
'''


class Node:
    def __init__(self,val=0,prev=None,next=None,child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child 

def flatten(head):

    if head is None:
        return head 

    dummy = Node(0,None,head,None)
    stack = [head]
    prev = dummy

    while len(stack) != 0:

        cur = stack.pop()
        
        prev.next = cur
        cur.prev = prev 

        if cur.next is not None:
            stack.append(cur.next)

        if cur.child is not None:
            stack.append(cur.child)
            cur.child = None
            # cur.next = cur.ch

        prev = cur

    dummy.next.prev = None 
    return dummy.next 


def printLinkedList(head):
    li = []
    temp = head
    while temp:
        li.append(temp.val)
        temp = temp.next
    print(li)



if __name__ == '__main__':
    headA = Node(1,None,None,None)
    ndB = Node(2,headA,None,None)
    ndC = Node(3,None,None,None)
    headA.next = ndB
    headA.child = ndC
    printLinkedList(headA)
    flatten(headA)
    printLinkedList(headA)