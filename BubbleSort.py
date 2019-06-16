n=int(input("Number of elements:"))
list=[input() for x in range(0,n)]
print("List before sorting:")
for x in range(0,n):
    print(list[x])
for x in range(0,n):
    for j in range(0,n-1):
        if(list[j]>list[j+1]):
            list[j],list[j+1]=list[j+1],list[j]
print("List after sorting:")
for x in range(0,n):
    print(list[x])                
