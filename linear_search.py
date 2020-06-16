from array import *

arr = array('i' , [])
n = int(input("Enter the size of array: "))
for i in range(n):
              x = int(input("enter the next value"))
              arr.append(x)
print(arr)
k = int(input("Enter the value to be searched: "))
x = 0
flag = 0
for i in arr:
    if i == k:
        print("Number FOUND at location: ",x)
        flag = 1
    x+=1
if flag == 0:
    print("Number NOT FOUND")

