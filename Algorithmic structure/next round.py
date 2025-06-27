n = input().split(" ")
N = list(map(int , n))
k = input().split(" ")
K = list(map(int,k))
def sapxep(B):
    for i in range(len(K)):
        for j in range(i,len(K)):
            if B[i] < B[j]:
                tg = B[i]
                B[i] = B[j]
                B[j] = tg

sapxep(K)
def SL(K,L):
    dem = 0
    for a in range(len(K)):
        if K[a] >= K[L-1] and K[a] > 0:
            dem += 1
    return dem

SL(K,N[1])
print(SL(K,N[1]))
