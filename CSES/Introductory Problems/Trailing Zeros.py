n=int(input())
def giaithua(n):
  if n == 0:
    return 0
  k = 1
  tz = 0
  while 5**k <= n:
    tz += n//5**k
    k += 1
  return tz
print(int(giaithua(n)))














