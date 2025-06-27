n = int(input())
a = input().split(" ")
S = list(map(int,a))
d=sum(S)
def Su(A):
    if (len(A)==0):
        return [0]
    sm = Su(A[1:len(A)])
    result = [0] * (2 * len(sm))
    k=0
    for i in range(len(sm)):
        result[k]=sm[i]
        k=k+1
    for i in range(len(sm)):
        if A[0]+sm[i] < (d//2)+1:
            result[k]=A[0]+sm[i]
            k=k+1
    return result
print(d-2*max(Su(S)))





