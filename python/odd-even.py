#Input

#arr:3 2 1 7 5 4

#Output

#7

#Explanation

#Second largest among even position elements(1 3 5) is 3
#Second smallest among odd position element is 4
#Thus output is 3+4 = 7
#Sample Input

#arr:1 8 0 2 3 5 6

#Sample Output

#8

arr=[1,8,0,2,3,5,6]

even=[]
odd=[]

for i in range(len(arr)):
    if i%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
print(even)
print(odd)
even.sort()
odd.sort()
print("Even after sort:",even)
print("odd after sort:",odd)
sum=even[len(even)-2]+odd[1]
print("Total sum:",sum)
