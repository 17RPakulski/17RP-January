def bubble_sort(L, descending = False, dbg= False):
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
    file.close()
    return("OUTPUT (sorted list): ", L)
        
        
    
listt = [4,1,3,2,45]
result = bubble_sort(listt, descending = True, dbg = True)



print('--', result)
