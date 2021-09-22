n = int(input())
arr = list(map(int, input().split()))
weights = list(map(int, input().split()))
print(round(sum([arr[x]*weights[x] for x in range(len(arr))]) / sum(weights), 1))
    
    
==>
    
5
10 40 30 50 20
1 2 3 4 5

32.0
