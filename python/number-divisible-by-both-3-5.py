n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
arr=[]
for i in range(n1,n2+1):
    if i%3== 0 and i%5==0:
        arr.append(i)
        10
print(sum(arr))