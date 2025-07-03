N = input("Enter the number: ")
sum = 0
for i in range (len(N)):
    digit=int(N[i])
    sum += (digit*10)+(i+1)
print(sum)