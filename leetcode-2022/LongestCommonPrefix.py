'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

# binary search version
def longestCommonPrefix(strs):
    if strs is None or len(strs) == 0:
        return ""
    
    minLen = 5000
    for i in strs:
        minLen = min(minLen,len(i))

    low = 1
    high = minLen

    while low <= high:
        mid = (low + high)//2
        if hasCommonPrefix(strs,mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return strs[0][0:(low+high)//2]

def hasCommonPrefix(strs,length):
    s = strs[0][0:length]
    for i in range(1,len(strs)):
        if not strs[i].startswith(s):
            return False
    return True

# Dynamic Programming based solution
def longestCommonPrefixDC(strs):
    if strs is None or len(strs) == 0:
        return ""
    return lcp(strs,0,len(strs) - 1)

def lcp(strs,left,right):
    if left == right:
        return strs[left]
    mid = (left + right) // 2
    ls = lcp(strs,left,mid)
    rs = lcp(strs,mid+1,right)
    return checkPrefix(strs,ls,rs)

def checkPrefix(strs,ls,rs):
    s1 = ""
    mini = min(len(ls),len(rs))
    for i in range(mini):
        if ls[i] != rs[i]:
            return ls[:i]
    return ls[:mini]


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))
    print(longestCommonPrefixDC(strs))
    strs = ["dog","racecar","car"]
    print(longestCommonPrefix(strs))
    print(longestCommonPrefixDC(strs))