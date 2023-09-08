from numpy import random
import pandas as pd
import os
import sorting

MAXARRAYSIZE = 1_000_000
LARGESTNUM = 100_000_000
SCRIPTPATH = os.path.dirname(__file__)

#
# part ci
#
# create a CSV file with column 1 as the arraySize (1000 to MAXARRAYSIZE), and remaining columns as number of key comparisons needed for different S (0 to 30) 
# for each row the randomIntegers array used for sorting is the same (ie a new randomIntegers array is only generated for each array size)
#
# todo: plot a line graph for each different value of S on excel
#

increment = 500
arraySize = 1000  # starting array size
oldArraySize = 1000 

comparisonsList = {'arraySize': []}
for s in range (0 , 31 , 3) :
    comparisonsList[f"keyComparisons_S{s}"] = []

# for each row
while arraySize <= MAXARRAYSIZE :

    comparisonsList['arraySize'].append (arraySize)
    randomIntegers = random.randint(1, LARGESTNUM, arraySize).tolist()

    # for each item in the row
    for s in range(0, 31, 3):

        randomIntegersCopy = randomIntegers.copy()

        numComparisons = sorting.mergeSortHybrid(randomIntegersCopy, s)
        comparisonsList[f"keyComparisons_S{s}"].append(numComparisons)

    arraySize += increment

    if arraySize == oldArraySize * 10 :
        oldArraySize = arraySize
        increment *= 10


df = pd.DataFrame (comparisonsList)
df.to_csv (f"{SCRIPTPATH}\\result\\compOverSize.csv" , index = False)

print ("Data recorded in result\\compOverSize.csv")
