flag = 0
count = 0
n = int(input("Enter the range: "))
print("Prime Numbers: ")
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, "  ", end = "")
        count += 1
    else:
        flag = 0
print("")
print("The total number of Prime Numbers in the given range are: ", count)

