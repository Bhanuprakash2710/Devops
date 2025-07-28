arr=[12,3,14,56,77,13]
num=13
diff=2
count=0
for i in arr:
    if abs(i-num)<=2:
        count+=1
print(count)