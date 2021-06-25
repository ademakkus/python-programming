N = int(input("Please input a 6-digit integer:"))
S = str(N)
RS = ""
for i in range(len(S) - 1, -1, -1):
    RS += S[i]
print(int(RS))
