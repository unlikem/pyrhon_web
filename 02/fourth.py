TempStr = input()
n = len(TempStr)
if TempStr[0:3] in ['RMB']:
    U = eval(TempStr[3:n]) / 6.78
    print("USD{:.2f}".format(U))
elif TempStr[0:3] in ['USD']:
    R = eval(TempStr[3:n]) * 6.78
    print("RMB{:.2f}".format(R))