from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import os
import sorting
import main

scriptPath = os.path.dirname(__file__)

#
# part ci: S fixed, plot number of key comparisons over diff size of input list n
#

S = int(input("Choose S: ")) # thereshold for size of subarray (switch from insertionSort to mergeSort)

multiplyIncre = bool( int( input ("Array size incremention method (0 for addition , 1 for multiplication): " ) ) )
increment = int (input ("Enter incrementation number: "))

arraySize = 1000  # aka n (starting array size)
comparisonsList = {'arraySize': [], 'keyComparisons': []}

while arraySize <= main.MAXARRAYSIZE :

    randomIntegers = random.randint(1, main.LARGESTNUM, arraySize).tolist()
    numComparisons = sorting.mergeSortHybrid(randomIntegers, S)

    comparisonsList['arraySize'].append(arraySize)
    comparisonsList['keyComparisons'].append (numComparisons)

    if multiplyIncre :
        arraySize *= increment
    else :
        arraySize += increment

df = pd.DataFrame (comparisonsList)
df.to_csv (f"{scriptPath}\\result\\compOverSize_S{S}.csv" , index = False)

print (f"Data recorded in result\\compOverSize_S{S}.csv")
