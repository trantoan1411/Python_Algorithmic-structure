n= int(input())
def giaithua(n):
    if n == 1:
        result = 1
    else:
        result = giaithua(n-1)*n
    return result
print(giaithua(n))



