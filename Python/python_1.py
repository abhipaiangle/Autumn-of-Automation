import math

def digits(x):
    i = 0
    while x!=0:
        x = int(x/10)
        i = i + 1
    return i
def isPrime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

dig = int(input())
i = 2
while dig >= digits(i+2):
    if isPrime(i) == True:
        if isPrime(i+2) == True:
            print(f"{i} {i+2}")
    i = i+1
