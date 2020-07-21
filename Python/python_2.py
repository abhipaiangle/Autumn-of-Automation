def isPal(x):
    num = 0
    c = x
    while x!=0:
        num = num*10 + x%10
        x = int(x/10)
    if num == c:
        return True
    else:
        return False

x = int(input())

while(True):
    if isPal(x+1) == True:
        print(x+1)
        break
    x = x+1