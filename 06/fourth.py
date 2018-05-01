# 列表操作

It = []
It += [1, 2, 3, 4, 5]
It[2] = 6
It.insert(2, 7)
del It[1]
del It[1:4]
0 in It
It.append(0)
It.index(0)
len(It)
max(It)

for item in It:
    print(item, end=" ")