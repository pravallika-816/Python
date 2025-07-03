num = int(input("Enter the number: "))
is_prime=True
for i in range (2,num):
    if (num % i == 0):
        is_prime = False
        break
if is_prime == True:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")