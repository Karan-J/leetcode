'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

'''



class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


visited = {}
    
def copyRandomList(head):
    # recursive
    if head is None:
        return None
    # if head.next is None:
    #     return Node(head.val,None,head.random)
    
    if head in visited:
        return visited[head]
    
    node = Node(head.val,None,None)
    
    visited[head] = node
    
    node.next = copyRandomList(head.next)
    node.random = copyRandomList(head.random)
    
    return node



vis = {}

def getClonedNode(node):
    if node is None:
        return node

    if node in vis:
        return vis[node]
    else:
        vis[node] = Node(node.val,None,None)
        return vis[node]
    return None

def copyRandomListIterative(head):
    if head is None:
        return head

    temp = head
    newHead = Node(temp.val,None,None)
    ptr = newHead
    
    while temp.next is not None:

        ptr.next = getClonedNode(temp.next)
        ptr.random = getClonedNode(temp.random)

        temp = temp.next
        ptr = ptr.next

    return newHead



def printLinkedList(head):
    li = []
    temp = head
    while temp:
        li.append(temp.val)
        temp = temp.next
    print(li)



def copyRandomListConstantSpace(head):

    if not head:
            return head

    # Creating a new weaved list of original and copied nodes.
    ptr = head
    while ptr:

        # Cloned node
        new_node = Node(ptr.val, None, None)

        # Inserting the cloned node just next to the original node.
        # If A->B->C is the original linked list,
        # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
        new_node.next = ptr.next
        ptr.next = new_node
        ptr = new_node.next

    ptr = head

    # Now link the random pointers of the new nodes created.
    # Iterate the newly created list and use the original nodes random pointers,
    # to assign references to random pointers for cloned nodes.
    while ptr:
        ptr.next.random = ptr.random.next if ptr.random else None
        ptr = ptr.next.next

    # Unweave the linked list to get back the original linked list and the cloned list.
    # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
    ptr_old_list = head # A->B->C
    ptr_new_list = head.next # A'->B'->C'
    head_new = head.next
    while ptr_old_list:
        ptr_old_list.next = ptr_old_list.next.next
        ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
        ptr_old_list = ptr_old_list.next
        ptr_new_list = ptr_new_list.next
    return head_new

    # if head is None:
    #     return None
    
    # temp = head 
    # printLinkedList(temp)
    
    # while temp is not None:
    #     nd = Node(temp.val,None,None)
    #     nd.next = temp.next
    #     temp.next = nd 
    #     temp = nd.next

    # printLinkedList(temp)
    # temp = head 
    # newHead = temp.next
    # newTemp = newHead

    # while temp is not None:
    #     temp.next.random = temp.random.next if temp.random is not None else None
    #     temp.next = temp.next.next
        
    # printLinkedList(newHead)

    # oldList = head
    # # newTemp.next = newTemp.next.next
    # while oldList is not None:
    #     oldList.next = oldList.next.next
    #     newTemp.next = newTemp.next.next if newTemp.next is not None else None
    #     oldList = oldList.next
    #     newTemp = newTemp.next

    # return newHead


if __name__ == '__main__':
    headA = Node(1)
    headA.next = Node(3)
    printLinkedList(headA)
    headB = copyRandomList(headA)
    printLinkedList(headB)
    headC = copyRandomListIterative(headA)
    printLinkedList(headC)
    print(vis)
    headC = None
    headC = copyRandomListConstantSpace(headA)
    printLinkedList(headC)