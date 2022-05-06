'''
Given two binary strings a and b, return their sum as a binary string.

 
Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

def addBinary(a,b):
    x = 0
    y = 0
    a = a[::-1]
    b = b[::-1]
    for i in range(len(a)):
        if a[i] == '1':
            x += 2**i
    for i in range(len(b)):
        if b[i] == '1':
            y += 2**i
    z = x + y
    print(x,y,z)
    return bin(z)[2:]

if __name__ == '__main__':
    a = '11'
    b = '1'
    print(addBinary(a,b))
    a = '1010'
    b = '1011'
    print(addBinary(a,b))
    a = '10010'
    b = '1011'
    print(addBinary(a,b))
