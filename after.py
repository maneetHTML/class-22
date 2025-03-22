l1=int(input("enter the number : "))
l2=int(input("enter the number : "))
lst=[]
for i in range(l1,l2+1):
    lst.append(i*i)
print(lst)
evenlst=[]
oddlst=[]
for i in lst:
    if i%2==0:
        evenlst.append(i)
    else:
        print("even list",evenlst)
        print("odd list",oddlst)
