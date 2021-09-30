# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
seq = 'IVXLCDM'

# 1 to 3999
num = 'LVIII'
# num = "MCMXCVI"
s = num
# val = 0
# l = 0
# current = num[0]
# for i in range(len(num)-1):
#     current = num[i]
#     next = num[i+1]
#     if(current=='I' and next=='V'):
#         val = val + 4
#     elif (current=='I' and next=='X'):
#         val += 9
#     elif (current=='X' and next=='L'):
#         val+=40
#     elif (current=='X' and next=='C'):
#         val+=90
#     elif (current=='C' and next=='D'):
#         val+=400
#     elif (current=='C' and next=='M'):
#         val+=900
#     else:
#         val = val + dic[num[i]]
#     print(val)
#
# last = num[-1]
# val = val + dic[num[i]]
# print(val)

copy = num
val = 0
i = 0
while num!='':
    print('----------',i, num)
    if 'IV' in num:
        num = num.replace('IV', '')
        val +=4
    if 'IX' in num:
        num = num.replace('IX', '')
        val+=9
    if 'XL' in num:
        num = num.replace('XL', '')
        val += 40
    if 'XC' in num:
        num = num.replace('XC', '')
        val += 90
    if 'CD' in num:
        num = num.replace('CD', '')
        val += 400
    if 'CM' in num:
        num = num.replace('CM','')
        val+=900
    else:
        temp = num[i]
        print('in else',temp, dic[temp],val)
        num = num.replace(num[0],'',1)
        val += dic[temp]
        # i += 1
    print(num, val)

t = "hello"
print(t.index("lo"))

print(t.find("lo"))



s = 'MCM'
dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
stack = []
print(s)
for i in range(1,len(s)):
    print(s[i-1],dic[s[i-1]],'----',s[i],dic[s[i]])
    if dic[s[i-1]]>=dic[s[i]]:
        stack.append(dic[s[i-1]])
    else:
        stack.append(-dic[s[i-1]])
    print(stack,'=========')
stack.append(dic[s[-1]])
print(stack)
res=0
for i in stack:
    res += i
print(res, "--------------------")


