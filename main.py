import re
import sys
import time
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# Driver code to test above
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/100.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array100 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/1000.txt') as f1:
    contents = f1.readlines()
    stripped = [s.strip() for s in contents]
    Array1000 = [int(x2) for x2 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/2000.txt') as f2:
    contents = f2.readlines()
    stripped = [s.strip() for s in contents]
    Array2000 = [int(x3) for x3 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/3000.txt') as f3:
    contents = f3.readlines()
    stripped = [s.strip() for s in contents]
    Array3000 = [int(x4) for x4 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/4000.txt') as f4:
    contents = f4.readlines()
    stripped = [s.strip() for s in contents]
    Array4000 = [int(x5) for x5 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/5000.txt') as f5:
    contents = f5.readlines()
    stripped = [s.strip() for s in contents]
    Array5000 = [int(x6) for x6 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/6000.txt') as f6:
    contents = f6.readlines()
    stripped = [s.strip() for s in contents]
    Array6000 = [int(x7) for x7 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/7000.txt') as f7:
    contents = f7.readlines()
    stripped = [s.strip() for s in contents]
    Array7000 = [int(x8) for x8 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/8000.txt') as f8:
    contents = f8.readlines()
    stripped = [s.strip() for s in contents]
    Array8000 = [int(x9) for x9 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/9000.txt') as f9:
    contents = f9.readlines()
    stripped = [s.strip() for s in contents]
    Array9000 = [int(x10) for x10 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/10000.txt') as f10:
    contents = f10.readlines()
    stripped = [s.strip() for s in contents]
    Array10000 = [int(x11) for x11 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/20000.txt') as f11:
    contents = f11.readlines()
    stripped = [s.strip() for s in contents]
    Array20000 = [int(x12) for x12 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/30000.txt') as f12:
    contents = f12.readlines()
    stripped = [s.strip() for s in contents]
    Array30000 = [int(x13) for x13 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/40000.txt') as f13:
    contents = f13.readlines()
    stripped = [s.strip() for s in contents]
    Array40000 = [int(x14) for x14 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/50000.txt') as f14:
    contents = f14.readlines()
    stripped = [s.strip() for s in contents]
    Array50000 = [int(x15) for x15 in stripped]
#%%
t1 = time.time()
bubbleSort(Array100)
print("--- %s seconds ---" % (time.time() - t1))
#%%
t2 = time.time()
bubbleSort(Array1000)
print("--- %s seconds ---" % (time.time() - t2))
#%%
t3 = time.time()
bubbleSort(Array2000)
print("--- %s seconds ---" % (time.time() - t3))
#%%
t4 = time.time()
bubbleSort(Array3000)
print("--- %s seconds ---" % (time.time() - t4))
#%%
t5 = time.time()
bubbleSort(Array4000)
print("--- %s seconds ---" % (time.time() - t5))
#%%
t6 = time.time()
bubbleSort(Array5000)
print("--- %s seconds ---" % (time.time() - t6))
#%%
t7 = time.time()
bubbleSort(Array6000)
print("--- %s seconds ---" % (time.time() - t7))
#%%
t8 = time.time()
bubbleSort(Array7000)
print("--- %s seconds ---" % (time.time() - t8))
#%%
t9 = time.time()
bubbleSort(Array8000)
print("--- %s seconds ---" % (time.time() - t9))
#%%
t10 = time.time()
bubbleSort(Array9000)
print("--- %s seconds ---" % (time.time() - t10))
#%%
t11 = time.time()
bubbleSort(Array10000)
print("--- %s seconds ---" % (time.time() - t11))
#%%
t12 = time.time()
bubbleSort(Array20000)
print("--- %s seconds ---" % (time.time() - t12))
#%%
t13 = time.time()
bubbleSort(Array30000)
print("--- %s seconds ---" % (time.time() - t13))
#%%
t14 = time.time()
bubbleSort(Array40000)
print("--- %s seconds ---" % (time.time() - t14))
#%%
t15 = time.time()
bubbleSort(Array50000)
print("--- %s seconds ---" % (time.time() - t15))
#%%
print("Sorted 100 array is:")
for i in range(len(Array100)):
    print("%d" % Array100[i], end=" ")
print("Sorted 1000 array is:")
for i2 in range(len(Array1000)):
    print("%d" % Array1000[i2], end=" ")
print("Sorted 2000 array is:")
for i3 in range(len(Array2000)):
    print("%d" % Array2000[i3], end=" ")
print("Sorted 3000 array is:")
for i4 in range(len(Array3000)):
    print("%d" % Array3000[i4], end=" ")
print("Sorted 4000 array is:")
for i5 in range(len(Array4000)):
    print("%d" % Array4000[i5], end=" ")
print("Sorted 5000 array is:")
for i6 in range(len(Array5000)):
    print("%d" % Array5000[i6], end=" ")
print("Sorted 6000 array is:")
for i7 in range(len(Array6000)):
    print("%d" % Array6000[i7], end=" ")
print("Sorted 7000 array is:")
for i8 in range(len(Array7000)):
    print("%d" % Array7000[i8], end=" ")
print("Sorted 8000 array is:")
for i9 in range(len(Array8000)):
    print("%d" % Array8000[i9], end=" ")
print("Sorted 9000 array is:")
for i10 in range(len(Array9000)):
    print("%d" % Array9000[i10], end=" ")
print("Sorted 10000 array is:")
for i11 in range(len(Array10000)):
    print("%d" % Array10000[i11], end=" ")
print("Sorted 20000 array is:")
for i12 in range(len(Array20000)):
    print("%d" % Array20000[i12], end=" ")
print("Sorted 30000 array is:")
for i13 in range(len(Array30000)):
    print("%d" % Array30000[i13], end=" ")
print("Sorted 40000 array is:")
for i14 in range(len(Array40000)):
    print("%d" % Array40000[i14], end=" ")
print("Sorted 50000 array is:")
for i15 in range(len(Array50000)):
    print("%d" % Array50000[i15], end=" ")
