n = int(input())
x = sorted(list(map(int,input().split())))

from statistics import median

print(int(median(x[:n//2])))
print(int(median(x)))
print(int(median(x[(n+1)//2:])))


==>

9
3 7 8 5 12 14 21 13 18

6
12
16
