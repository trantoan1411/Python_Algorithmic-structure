a = int(input())
b = input().split(" ")
c = list(map(int, b))
c.sort()
c.append("")
i=1
while True:
    if i == c[i-1]:
        i += 1
    else:
        print(i)
        break


