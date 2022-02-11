def lcs(x, y, a, b):
    L = [[0 for x in range(b + 1)] for x in range(a + 1)]
    for i in range(a + 1):
        for j in range(b + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[a][b]
    lcs = [""] * (index + 1)
    lcs[index] = ""
    i = a
    j = b
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs[index - 1] = x[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print("LCS of " + x + " and " + y + " is " + "".join(lcs))


X = "GTAG"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
lcs(X, Y, m, n)
