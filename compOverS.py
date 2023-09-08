from numpy import random
import pandas as pd
import os
import sorting

MAXARRAYSIZE = 1_000_000
LARGESTNUM = 100_000_000
SCRIPTPATH = os.path.dirname(__file__)

#
# part cii
#
# fix arraySize as 1 million, create a CSV file with column 1 as S (0 to 40), and remaining columns as the number of key comparisons needed for different randomly generated list
# for each column the randomIntegers array is the same (ie as S varies the randomIntegers array used for sorting is the same)
#
# todo: create an average key comparisons column in excel and plot a graph from that
#

arraySize = 100_000

comparisonsList = {'S': list (range (41))}

# for each column
for i in range (1 , 11) :

    comparisonsList[f"keyComparisons{i}"] = []
    randomIntegers = random.randint(1, LARGESTNUM, arraySize).tolist()

    # for each item in the column
    for s in range (41) :

        randomIntegersCopy = randomIntegers.copy()

        numComparisons = sorting.mergeSortHybrid(randomIntegersCopy, s)
        comparisonsList[f'keyComparisons{i}'].append(numComparisons)


df = pd.DataFrame(comparisonsList)
df.to_csv(f"{SCRIPTPATH}\\result\\compOverS_arraySize.csv", index=False)

print("Data recorded in result\\compOverS_arraySize.csv")
