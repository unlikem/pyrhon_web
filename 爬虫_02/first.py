import math


def isPrime(num):
    if num == 1:
        return False
    k = int(math.sqrt(num))
    for i in range(2, k + 1, 1):
        if num % i == 0:
            return False
    return True


def prime(num):
    if num == 1:
        return 2
    k = 1
    i = 1
    while(k < num):
        i += 2
        if(isPrime(i) == True):
            k += 1
    return i

def monisen(no):
    k=0
    i=1
    t=0
    while(k<no):
        t=prime(i)
        if(isPrime(2**t-1)==True):
            k+=1
        i+=1
    return 2**t-1

print(monisen(int(input())))



