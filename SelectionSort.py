list=[2,7,4,1,5,3]
n=len(list)
print("List before sorting: ")
for i in range(n):
    print(list[i])
print()
for i in range(n):
    imin=i
    for j in range(i+1,n):
        if list[j]<list[imin]:
            imin=j
    list[i],list[imin]=list[imin],list[i]
print("After sorting: ")
for i in range(n):
    print(list[i])
