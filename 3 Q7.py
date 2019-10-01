for j in range(0,51):
    if j>=1:
        for i in range(2,j):
            if j%i==0:
                break
        else:
                print(j)
