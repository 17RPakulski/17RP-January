# working

# Simple (Selection) Sort

def selectionSort(L, descending = True):
    # 1. Initialise an unsorted list
    # 2. Initialise a marker
    marker = 0
    
    # 3. Traverse through all list items
    while marker < len(L):
        # 4. Find the minimum item to the right of the marker
        index_of_min = marker
        #if descending:
        for j in range(marker+1, len(L)):
            if descending:
                if L[index_of_min] < L[j]:
                    index_of_min = j
            else:
                if L[index_of_min] > L[j]:
                     index_of_min = j
                        # 5. Exchange the smallest item with the item at the marker
        temp = L[marker] # save the item at the marker
        L[marker] = L[index_of_min] # copy 1
        L[index_of_min] = temp # copy 2
    # 6. Advance the marker to the right by 1 position
        marker = marker+1
                #return('output: '+ str(L))
            
            

# 7. Stop

L = [9, 6, 10, 4, 8, 5, 7]
selectionSort(L, descending = True)
print(L)


