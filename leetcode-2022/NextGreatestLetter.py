'''
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"
 

Constraints:
2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
'''


def myNextGreatestLetter(letters, target):
    lets = 'abcdefghijklmnopqrstuvwxyz'
    li = list(lets)
    left = 0
    right = len(li) - 1

    def linSearch(letters,li,mid):
        for i,v in enumerate(letters):
            if v > li[mid]:
                return i
        return 0

    while left <= right:
        mid = left + (right - left) // 2
        if li[mid] == target:
            ind = linSearch(letters,li,mid)
            return letters[ind]
        elif target < li[mid]:
            right = mid - 1
        else:
            left = mid + 1

# linear search
def linNextGreatestLetter(letters,target):
    for l in letters:
        if l > target:
            return l
    return letters[0]

# binary search 
def binNextGreatestLetter(letters, target):
    left = 0
    right = len(letters)

    while left < right:
        mid = left + (right - left) // 2
        if target < letters[mid]:
            right = mid 
        else:
            left = mid + 1
    
    return letters[left % len(letters)]



if __name__ == '__main__':
    letters = ["c","f","j"]
    target = "a"
    print(myNextGreatestLetter(letters,target='a'),linNextGreatestLetter(letters,'a'),binNextGreatestLetter(letters,'a'))
    print(myNextGreatestLetter(letters,'c'),linNextGreatestLetter(letters,'c'),binNextGreatestLetter(letters,'c'))
    print(myNextGreatestLetter(letters,'f'),linNextGreatestLetter(letters,'f'),binNextGreatestLetter(letters,'f'))
    print(myNextGreatestLetter(letters,'j'),linNextGreatestLetter(letters,'j'),binNextGreatestLetter(letters,'j'))