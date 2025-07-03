n = int(input("Enter the number: "))
ori = n
rev = 0
while n > 0:
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
if ori == rev:
    print(f"{ori} is a Palindrome")
else:
    print(f"{ori} is not a Palindrome")
