n = input("Enter the number: ")
ori = int(n)
sum = 0
N = len(n)
n = int(n)
while n > 0:
    rem = n % 10
    sum += rem ** N
    n = n // 10
if ori == sum:
    print(f"{ori} is a Armstrong Number")
else:
    print(f"{ori} is not a Armstrong Number")
