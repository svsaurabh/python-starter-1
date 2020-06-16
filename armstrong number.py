sum = 0
n = int(input("Enter a number: "))
temp = n
while n != 0:
    remainder = n % 10
    sum = sum + remainder**3
    n = n // 10
if sum == temp:
    print("It is an ARMSTRONG NUMBER!!!")
else:
    print("It is not an ARMSTRONG NUMBER!!!")