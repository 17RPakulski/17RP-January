#add in hashtags and this isnt complete, WROONGGGG coz the if and else things
def bubble_sort(L, descending = False, dbg= False):
    if dbg:
        fo = open('log.txt', 'w')
        
    print("INPUT (initial list): ", L)
    exchange = True
    n = len(L)
    i = 0
    while (i< n) and  exchange:
        print("BEFORE PASS %d: %s " %(i+1, L))
        exchange = False
        for j in range(n-i-1):
            
            print("%s " %L, end="-> ")
            if descending:
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    exchange = True 
                    print("%s " %L)
                else:
                    if L[j] < L[j+1]:
                        L[j], L[j+1] = L[j+1], L[j]
                        exchange = True 
                        print("%s " %L)
                    
        print("AFTER PASS %d: %s " %(i+1, L))
        i= i+1 
    return("OUTPUT (sorted list): ", L)
        
listt = [4,1,3,2,45]
result = bubble_sort(listt, descending = True)

print('--', result)