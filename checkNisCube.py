N=input("Please input and integer number:")
N=int(N)
M=N**(1/3)
if int(M**3)==N:
    print(True)
else:
    print(False)
