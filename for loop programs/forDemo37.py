#nested loop
for i in range(1,6):
    for j in range(1,6):
        if (j==3):
            break
        print(i,j)
    if (i == 3):
        break
    print()