mylist=[9,45,4,5]
sum=0
for i in mylist:
    sum=sum+i
print("total : " ,sum)
noofi=len(mylist)
av=sum/noofi
print("Average : " ,av)
print("Largest element" ,max(mylist))
print("Small element" ,min(mylist))