'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

'''

def editDistanceRec(word1,word2):
    x = len(word1)
    y = len(word2)
    if x == 0:
        return y 
    elif y == 0:
        return x 

    unequal = 1 if word1[-1] != word2[-1] else 0
    return min(editDistanceRec(word1[:-1],word2) + 1, editDistanceRec(word1,word2[:-1]) + 1, editDistanceRec(word1[:-1],word2[:-1]) + unequal)

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(editDistanceRec(word1,word2))
    word1 = "intention"
    word2 = "execution"
    print(editDistanceRec(word1,word2))
    # word1 = "dinitrophenylhydrazine"
    # word2 = "acetylphenylhydrazine"
    # print(editDistanceRec(word1,word2))