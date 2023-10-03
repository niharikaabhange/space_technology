ls = [1, 6, 3, 4, 3, 5]

change = 1

while change == 1:
    change = 0
    newls = []
    newls.append(ls[0])

    for i in range(1, len(ls)- 1):
        if (ls[i - 1] < ls[i]) and (ls[i + 1] < ls[i]):
            newls.append(ls[i] - 1)
            change = 1
        elif (ls[i - 1] > ls[i]) and (ls[i + 1] > ls[i]):
            newls.append(ls[i] + 1)
            change = 1
        else:
            newls.append(ls[i])

    newls.append(ls[-1])
    ls = newls
    print(newls)

        
print(newls)
        


