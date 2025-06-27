n = int(input())
print(2**n-1)
def Tower(n, a,b, c):
    if n == 1:
        print(a,b)
        return
    Tower(n - 1,a,c,b)
    print(a,b)
    Tower(n - 1, c, b, a)

Tower(n, '1', '3', '2')

















