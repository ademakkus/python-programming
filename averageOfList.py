clas_grades=[[8,80,60,80],[88,18,65,81],[86,89,69,82]]
row=0
while row<len(clas_grades):
    SUM=0
    col=0
    while row<len(clas_grades[row]):
        SUM+=clas_grades[row][col]
        col+=1
        Avg=SUM/len(clas_grades[row])
        print(Avg)
        row+=1