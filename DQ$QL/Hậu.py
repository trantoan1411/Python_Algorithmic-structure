X=[0, 1, 2, 3, 4, 5, 6, 7]
Y= [7, 2, 0, 5, 1, 4, 6, 3]
map=["",
"",
"",
"",
"",
"",
"",
""]

for i in range(8):
    for j in range(8):
        if j==Y[i]:
            map[i]+="*"
        else:
            map[i]+="."

for k in range(8):
    print(map[k])
