N = input("Please input and integer number with 3 or more digits:")
if len(N) % 2 == 0:
    FH = N[:len(N) // 2]
    SH = N[len(N) // 2:]
else:
    FH = N[:len(N) // 2]
    SH = N[len(N) // 2 + 1:]
if int(FH) >= int(SH):
    print(True)
else:
    print(False)
