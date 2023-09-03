# return number of key comparisons
def insertionSort (array) :

    keyComparisons = 0 

    for i in range (1 , len (array)) :
        for j in range (i , 0 , -1) :

            keyComparisons += 1

            if (array[j] < array[j - 1]) :
                temp = array[j] 
                array[j] = array[j - 1]
                array[j - 1] = temp 
            else :
                break
    
    return keyComparisons

# original merge sort
# return number of key comparisons
def mergeSortOriginal (array) :

    keyComparisons = 0 

    if len (array) <= 1 :
        return keyComparisons
    
    mid = len (array) // 2

    L = array[:mid]
    keyComparisons += mergeSortOriginal (L)

    R = array[mid:] 
    keyComparisons += mergeSortOriginal (R)

    i = j = k = 0 

    while i < len (L) and j < len (R) :        
        if (L[i] < R[j]) :
            array[k] = L[i]
            i += 1
        else :
            array[k] = R[j]
            j += 1

        k += 1
        keyComparisons += 1

    while i < len (L):
        array[k] = L[i]
        k += 1
        i += 1
    
    while j < len (R) :
        array[k] = R[j]
        k += 1
        j += 1
    
    return keyComparisons

# merge sort with integrated insertion sort
# return number of key comparisons
def mergeSortHybrid(array , S):

    keyComparisons = 0

    if len(array) <= 1:
        return keyComparisons
    
    if len (array) <= S:
        return insertionSort (array)

    mid = len(array) // 2

    L = array[:mid]
    keyComparisons += mergeSortHybrid(L , S)

    R = array[mid:]
    keyComparisons += mergeSortHybrid(R , S)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if (L[i] < R[j]):
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1

        k += 1
        keyComparisons += 1

    while i < len(L):
        array[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        array[k] = R[j]
        k += 1
        j += 1

    return keyComparisons

