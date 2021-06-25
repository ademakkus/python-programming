def longRunZeros(s):
    big = 0
    curr = 0
    for c in s:
        if c == '0':
            curr += 1
        else:
            if curr > big:
                big = curr
            curr = 0
    if curr > big:
        big = curr
    return big

block=input('Enter a block:')
#print(longRunZeros('00100110100000111000000011'))
print(longRunZeros(block))
