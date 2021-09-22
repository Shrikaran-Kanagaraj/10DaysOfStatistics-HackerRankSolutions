import numpy as np
from scipy import stats

n = int(input())
arr = list(map(int,input().split()))

print(np.mean(arr))
print(np.median(arr))
print(stats.mode(arr)[0][0])


==>
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

43900.6
44627.5
4978
