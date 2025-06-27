n = int(input())
k = input().split(" ")
K = list(map(int,k))
def ABC(X):
    dem=0
    max=X[0]
    min=X[0]
    for j in range(len(X)):
        if K[j]>max or K[j]< min:
            if K[j]> max:
                max=K[j]
            if K[j]< min:
                min=K[j]
            dem+=1
    return dem
print(ABC(K))
