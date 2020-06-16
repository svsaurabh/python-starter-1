n = int(input("Enter a number: "))
temp = n
rev = 0
while n != 0:
    remainder = n % 10
    rev = rev * 10 + remainder
    n = n // 10
print("Reversed number: ", rev)
if temp == rev:
    print("It is a PALINDROME number!!!")
else:
    print("It is NOT A PALINDROME number!!!")

