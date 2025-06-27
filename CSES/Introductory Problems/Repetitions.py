a=input()
i=0
max=1
dem=1
while i < len(a)-1:
    if a[i] == a[i+1]:
        i+=1
        dem+=1
        if dem > max:
            max=dem
    else:
        if dem  > max:
            max = dem
        i+=1
        dem=1
print(max)
