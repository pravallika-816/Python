n1, n2 = 0, 1
n=int(input("Enter the length of series: "))
for i in range (0,n):
    print(n1, end=" ")
    next_num = n1 + n2
    n1 = n2
    n2 = next_num
    