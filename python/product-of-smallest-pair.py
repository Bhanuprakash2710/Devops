#Input

#sum:9

#size of Arr = 7

#Arr:5 2 4 3 9 7 1

#Output

#2

#Explanation

#Pair of least two element is (2, 1) 2 + 1 = 3 < 9, Product of (2, 1) 2*1 = 2. Thus, output is 2

#Sample Input

#sum:4

#size of Arr = 6

#Arr:9 8 3 -7 3 9

#Sample Output

#-21
n = int(input())
sum1 = int(input())
arr = list(map(int, input().split()))
arr.sort()
newarr=[]
newarr.append(arr[0])
newarr.append(arr[1])
print(newarr)

if sum(newarr)<=sum1:
    print(newarr[0]*newarr[1])
else:
    print("0")