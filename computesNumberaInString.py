string="happy new year"
for i in range(len(string)):
    if 'y'==string[i]:
        N1=i
        break
for i in range(len(string)-1,-1,-1):
    if 'y'==string[i]:
        N2=i
        break
print(N1,N2)