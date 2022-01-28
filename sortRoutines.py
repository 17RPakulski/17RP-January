def bubbleSort(L, descending = False, dbg= False):
    if dbg:
        file = open('log.txt', 'w')
        
    if dbg:
        file.write("INPUT (initial list): " + str(L)+ '\n')
    
    exchange = True
    n = len(L)
    i = 0
    while (i< n) and  exchange:
        if dbg:
            file.write('BEFORE PASS :' +str(i+1)+ str(L) + '\n')
        exchange = False
        for j in range(n-i-1):
            
            if dbg:
                file.write(str(L) + "-> \n")
            
            if descending:
                if L[j] < L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    exchange = True
                    if dbg:
                        file.write(str(L) + '\n')
            else:
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    exchange = True
                    if dbg:
                        file.write(str(L) + '\n')
        if dbg:        
            file.write("AFTER PASS :" + str(i+1) + str(L) + '\n')
        i= i+1
        
    if dbg:
        file.write('Result =' + str(L))
    
    return("OUTPUT (sorted list): ", L)

def insertionSort(L, descending = True):
    
    # 2. Initialise a marker​
    marker = 1
    
    while (marker < len(L)):

        # 4. Insert the selected item to its correct position​

        j = marker
        if descending:
            while (L[j] > L[j-1] and j>0):

                tmp = L[j]

                L[j] = L[j-1]

                L[j-1] = tmp

                j = j-1
        else:
            while (L[j] < L[j-1] and j>0):

                tmp = L[j]

                L[j] = L[j-1]

                L[j-1] = tmp

                j = j-1
            
        marker = marker+1


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


