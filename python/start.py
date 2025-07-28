r=7
unit=2
arr=[2,8,3,5,7,4,1,2]
n=8
sum=0
totalsum=r*unit
house=0
if n==0:
    print("-1")
for house in arr:
    sum=sum+arr[0]
    if sum>=totalsum:
       # print("food sufficient for r in ",i+1)
        break
if totalsum>sum:
    print("0") 
print(house+1)
    
    