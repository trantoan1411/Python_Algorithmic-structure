n=int(input())
a=2
for i in range(1, n):
    a=(a%(10**9+7)*2)%(10**9+7)
print(a)



