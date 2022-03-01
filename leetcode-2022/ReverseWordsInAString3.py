'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''


def reverseWords(s: str) -> str:
    l = list(s.split(' '))
    ans = ''
    ll = []
    for i in l:
        ll.append(i[::-1] + ' ')
    
    for j in ll:
        ans += j
    
    return ans[:-1]

def reverseWordsShorter(s):
    l = s.split(' ')
    ans = ''
    for i in l:
        w = i[::-1]
        ans += w + ' '
    return ans[:-1]

def reverseWordsAlternate(s):
    l = s.split(' ')
    out = []
    for i in l:
        out.append(i[::-1])
    return ' '.join(out)

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(reverseWords(s))
    print(reverseWordsShorter(s))
    print(reverseWordsAlternate(s))
    s = 'God Ding'
    print(reverseWords(s))
    print(reverseWordsShorter(s))
    print(reverseWordsAlternate(s))