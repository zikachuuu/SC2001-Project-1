from numpy import random
import pandas as pd
import os
import sorting
from globalData import MAXARRAYSIZE, LARGESTNUM

scriptPath = os.path.dirname(__file__)

#
# part ci: fix an S, create a CSV file with column 1 as the arraySize (1000 to 10 million), and column 2 as number of comparisons needed
#

S = int(input("Choose S: "))  # threshold for size of subarray (switch from insertionSort to mergeSort)

multiplyIncre = bool(int(input("Array size incrementation method (0 for addition , 1 for multiplication): ")))
increment = int(input("Enter incrementation number: "))

arraySize = 1000  # aka n (starting array size)
comparisonsList = {'arraySize': [], 'keyComparisons': []}

while arraySize <= MAXARRAYSIZE:

    sortedIntegers = list(range(arraySize))
    numComparisons = sorting.mergeSortHybrid(sortedIntegers, S)

    comparisonsList['arraySize'].append(arraySize)
    comparisonsList['keyComparisons'].append(numComparisons)

    if multiplyIncre:
        arraySize *= increment
    else:
        arraySize += increment

df = pd.DataFrame(comparisonsList)
df.to_csv(f"{scriptPath}\\result\\compOverSize_S{S}.csv", index=False)

print(f"Data recorded in result\\compOverSize_S{S}.csv")
