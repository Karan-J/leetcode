'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''

from functools import lru_cache

def longestCommonSubsequence(text1, text2):
    
    @lru_cache(maxsize=None)
    def memo_solve(p1, p2):
        
        # Base case: If either string is now empty, we can't match
        # up anymore characters.
        if p1 == len(text1) or p2 == len(text2):
            return 0
        
        # Recursive case 1.
        if text1[p1] == text2[p2]:
            return 1 + memo_solve(p1 + 1, p2 + 1)
        
        # Recursive case 2.
        else:
            return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
        
    return memo_solve(0, 0)


def lcs(text1, text2):
    dp_table = [[0]*(len(text2) + 1) for _ in range(len(text1) + 1)]
    for col in reversed(range(len(text2))):
        for row in reversed(range(len(text1))):
            if text1[row] == text2[col]:
                dp_table[row][col] = 1 + dp_table[row + 1][col + 1]
            else:
                dp_table[row][col] = max( dp_table[row][col + 1], dp_table[row + 1][col] )
    
    return dp_table[0][0]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace" 
    print(longestCommonSubsequence(text1,text2), lcs(text1,text2))
    text1 = "abc"
    text2 = "abc"
    print(longestCommonSubsequence(text1,text2), lcs(text1,text2))
    text1 = "abc"
    text2 = "def"
    print(longestCommonSubsequence(text1,text2), lcs(text1,text2))
    text1 = "acgtagca"
    text2 = "cgthccgta"
    print(longestCommonSubsequence(text1,text2), lcs(text1,text2))