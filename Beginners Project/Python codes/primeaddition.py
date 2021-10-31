print("Enter a limit")
end = int(input())
sum = 0
 
for i in range(1, end+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            sum=sum+i
print("sum is",sum)
