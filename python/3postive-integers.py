
#( a+ b ) , if c=1
#( a – b ) , if c=2
#( a * b ) ,  if c=3
#(a / b) ,  if c =4
#Assumption : All operations will result in integer output.

#Example:

#Input
#c :1
#a:12
#b:16
#Output:
#Since ‘c’=1 , (12+16) is performed which is equal to 28 , hence 28 is returned.

c,a,b=map(int,input().split())

if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)