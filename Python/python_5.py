n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
max_profit = 0
for i in range(0,n-1):
    min_ = a[i]
    max_ = max(a[i+1:])
    if max_- min_ >= max_profit:
        max_profit = max_ - min_
        index = i+1
    
if max_profit > 0:
    print(max_profit)
    print(index)

else:
    print("  No profit ")
