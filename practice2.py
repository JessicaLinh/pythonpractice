def findnums (numbers, numtofind):
    for i in numbers:
        if i == numtofind:
            return i   
    return -1


var1 = [7, 8, 3, 6, 4, 5, 1, 52, 730, 546]
rc = findnums (var1, 5)

print (rc)
