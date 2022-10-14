a = [23, 54, 43, 12, 5, 76, 5]

max = a[0]

for i in range(0, len(a)):
    if (a[i] > max):
        max = a[i]
print("largest number is : ", max)
