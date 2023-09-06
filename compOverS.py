from numpy import random
import pandas as pd
import os
import sorting
from globalData import MAXARRAYSIZE , LARGESTNUM

scriptPath = os.path.dirname(__file__)

#
# part cii: fix an input size n (size of array to be sorted), create a CSV file with column 1 as S (1 to the chosen n), and column 2 as the number of comparisons needed
#

arraySize = int (input ("Enter array size: "))

multiplyIncre = bool( int( input ("S incremention method (0 for addition , 1 for multiplication): " ) ) )
increment = int (input ("Enter incrementation number: "))

S = 1 # thereshold for size of subarray (switch from insertionSort to mergeSort)
comparisonsList = {'S': [], 'keyComparisons': []}

while S <= arraySize :

    randomIntegers = random.randint(1, LARGESTNUM, arraySize).tolist()
    numComparisons = sorting.mergeSortHybrid(randomIntegers, S)

    comparisonsList['S'].append(S)
    comparisonsList['keyComparisons'].append(numComparisons)

    if multiplyIncre:
        S *= increment
    else:
        S += increment

df = pd.DataFrame(comparisonsList)
df.to_csv(f"{scriptPath}\\result\\compOverS_arraySize{arraySize}.csv", index=False)

print(f"Data recorded in result\\compOverS_arraySize{arraySize}.csv")
