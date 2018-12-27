def reverseInteger(self, n):
    # write your code here
    if n < 0:
        number = n * (-1)
    else:
        number = n
    aa = list(str(number))
    #aa.reverse()
    number = 0
    for i in range(0, len(aa)):
        number = number + int(aa[i]) * (10 ** i)

    if n < 0:
        return number * (-1)
    else:
        return number

print(reverseInteger(1,321))