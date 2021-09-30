# Input: "()"
# Output: true
# Input: "()[]{}"
# Output: true
# Input: "(]"
# Output: false
# Input: "([)]"
# Output: false
# Input: "{[]}"
# Output: true
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

s="()[]{}"
valid = ''
if s=="":
    print(True)
elif len(s)%2!=0:
    print(False)
else:
    for i in range(1,len(s)):
        if s[i-1]=='(':
            if s[i]==')':
                print(True)
                valid+='()'
            elif s[i]=='[':
                continue
            elif s[i]=='{':
                continue
            else:
                print(False)
        elif s[i-1]=='[':
            if s[i]==']':
                print(True)
                valid += '[]'
            elif s[i]=='(':
                continue
            elif s[i]=='{':
                continue
            else:
                print(False)
        elif s[i-1]=='{':
            if s[i]=='}':
                print(True)
                valid += '{}'
            elif s[i]=='(':
                continue
            elif s[i]=='[':
                continue
            else:
                print(False)
        else:
            print(False)
        print(valid)

valid = True
s="()[]{}"
print(s.index(']'),s.index('['),list(s),s.find("}"),)
def val(s):
    if s == '':
        return  True
    elif len(s)%2!=0:
        return  False
    else:
        l = []
        dic = {']': '[', '}': '{', ')': '('}
        for i in s:
            # print(i, i in dic)
            if i not in dic:
                l.append(i)
            else:
                top = l.pop() if l else '#'
                if dic[i] != top:
                    return False
        return not l

print(val(s))

l = []
if l:
    print(3)
else:
    print(1)
