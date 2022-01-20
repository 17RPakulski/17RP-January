# Bubble Sort v1
# 1. Initialise an unsorted list
L= [5, 7, 3, 6, 2]

print("INPUT (initial list): ", L)

# 2. Traverse across every element in the list
for i in range(len(L)):
    # 3. Compare all adjacent elements starting from the beginning
    for j in range(len(L)-1):
        # 4. if the elements are out of order, then swap them
        if L[j] > L[j+1]:
            temp = L[j+1]
            L[j+1] = L[j]
            L[j] = temp
            
print("OUTPUT (sorted list): ", L)