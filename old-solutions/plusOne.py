def plusOne(digits):
    temp = digits[-1]
    if temp == 9 and len(digits) != 1:
        # digits[-1] = 0
        # digits[-2] = digits[-2] + 1
        l = []
        l += plusOne(digits[:-1])
        l.append(0)
        return l
    elif temp == 9:
        return [1, 0]
    else:
        digits[-1] = digits[-1] + 1
    return digits

l = [9,9,9,8]
print(l[:-1])

print(plusOne(l))