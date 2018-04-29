TempStr = input()
n = len(TempStr)
if TempStr[-1] in ['J']:
    C = eval(TempStr[0:-1]) / 4.186
    print("{:.3f}cal".format(C))
# print(TempStr[n-3:n])
if TempStr[n-3:n] in ['cal']:
    J = eval(TempStr[0:n-3]) * 4.186
    print("{:.3f}J".format(J))