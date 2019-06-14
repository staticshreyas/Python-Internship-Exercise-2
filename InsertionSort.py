list=[7,2,4,1,5,3]
n=len(list)
for i in range(1,n):
    value=list[i]
    hole=i
    while(hole>0 and list[hole-1]>value):
        list[hole]=list[hole-1]
        hole-=1
    list[hole]=value
for i in range(n):
    print(list[i])    
