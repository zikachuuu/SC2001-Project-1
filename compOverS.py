from numpy import random
import pandas as pd
import matplotlib.pyplot as plt
import os
import sorting
import main

scriptPath = os.path.dirname(__file__)

#
# part cii: input size n fixed, plot number of key comparisons over diff S
#

arraySize = int (input ("Enter array size: "))

multiplyIncre = bool( int( input ("S incremention method (0 for addition , 1 for multiplication): " ) ) )
increment = int (input ("Enter incrementation number: "))

S = 1 # thereshold for size of subarray (switch from insertionSort to mergeSort)
comparisonsList = {'S': [], 'keyComparisons': []}

while S <= arraySize :

    randomIntegers = random.randint(1, main.LARGESTNUM, arraySize).tolist()
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
