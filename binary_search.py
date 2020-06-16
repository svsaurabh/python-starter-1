lst = list()
n = int(input("Enter the size of array: "))
for i in range(n):
    lst.append(int(input("Enter the next value: ")))
print(lst)
search = int(input("\n Enter element to be searched: "))
l = 0
u = n-1
flag = 0
while l <= u:
    mid = (l+u)//2
    if search == lst[mid]:
        print("NUMBER FOUND!")
        flag = 0
        break
    elif search < lst[mid]:
        u = mid - 1
        flag = 1
    elif search > lst[mid]:
        l = mid + 1
        flag = 1
if flag == 1:
    print("NUMBER NOT FOUND!")

