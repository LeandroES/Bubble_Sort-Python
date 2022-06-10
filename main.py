import re
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
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/1000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array1000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/2000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array2000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/3000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array3000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/4000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array4000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/5000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array5000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/6000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array6000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/7000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array7000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/8000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array8000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/9000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array9000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/10000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array10000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/20000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array20000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/30000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array30000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/40000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array40000 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\BubbleSort-Python\data/50000.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array50000 = [int(x) for x in stripped]
bubbleSort(Array100)
print("Sorted array is:")
for i in range(len(intArray)):
    print("%d" % intArray[i], end=" ")
#%%

