#Example

#Input
#n:4
#m:20
#Output
#90

#Explanation

#Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60
#Sum of numbers not divisible by 4 are 1 +2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150
#Difference 150 – 60 = 90
#Sample Input
#n:3
#m:10
#Sample Output
#19
n=int(input("Enter a divisible number:"))
m=int(input("enter the range:"))
div=0
notdiv=0
for i in range(1,m+1):
    if i%n==0:
        div+=i
    else:
        notdiv+=i
solution=notdiv-div
print(solution)
