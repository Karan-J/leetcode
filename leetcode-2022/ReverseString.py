'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
'''

from typing import List

def reverseString(s:List[str]) -> None:
    if len(s) == 1:
        return s

    i = 0
    j = len(s) - 1
    while i < j//2:
        s[i],s[j] = s[j],s[i]
        i += 1
        j -= 1

    # return
    return s

def reverseStringRecursive(s:List[str]) -> None:
    def helper(left,right,s):
        if left < right:
            # print(s[left],s[right])
            s[left], s[right] = s[right], s[left]

            return helper(left+1,right-1,s)
    
    # return 
    helper(0,len(s) - 1,s)
    # print(s)
    return s

# need to return in order to show the output

if __name__ == '__main__':
    print(reverseString(list('Karan')))
    print(reverseString(list('Hannah')))
    print(reverseString(list('Leetcode')))
    print(reverseStringRecursive(list('String')))
    print(reverseStringRecursive(list('Leetcode')))