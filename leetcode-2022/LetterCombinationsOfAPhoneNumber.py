'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

'''

def letterCombinations(digits):
    dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    
    if len(digits) == 0:
        return []

    def backtrack(index,path):
        if len(path) == len(digits):
            out.append("".join(path))
            return

        possibleLetters = dic[digits[index]]
        for letter in possibleLetters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()


    out = []
    backtrack(0,[])
    return out


if __name__ == '__main__':
    digits = ""
    print(letterCombinations(digits))
    digits = "2"
    print(letterCombinations(digits))
    digits = "23"
    print(letterCombinations(digits))
    digits = "73"
    print(letterCombinations(digits))