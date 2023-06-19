ls = []
for i in range(0,5,1):
    n = int(input("Enter number = "))
    ls.append(n)
print("List: \n",ls)
print("Sum of all elements = ",sum(ls))
print("Smallest number = ",min(ls))
print("Biggest number = ",max(ls))
ls.sort()
print("Ascending = ",ls)
ls.reverse()
print("Descending = ",ls)
ls.sort()
print(tuple(ls))
del ls 