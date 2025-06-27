a=input()
dem=0
for b in a:
    if b.isupper():
        dem+=1
if dem > len(a)- dem:
    print(a.upper())
else:
    print(a.lower())
