x = int(input("Enter the number to check: "))
a = 0
b = 1

if x == 0:
    print("It is a FIBONACCI NUMBER!!!")
    exit()
while True:
    c = a + b
    a = b
    b = c
    if c >= x:
        break
if c == x:
    print("It is a FIBONACCI NUMBER!!!")
else:
    print("It is NOT A FIBONACCI NUMBER!!!")