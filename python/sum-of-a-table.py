n=int(input("Enter a number:"))
arr=[]

for i in range(1,11):
    x=i*n
    arr.append(x)
print(sum(arr))