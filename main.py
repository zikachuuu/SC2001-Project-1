from numpy import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import os

MAXARRAYSIZE = 10_000_000  # max array size
LARGESTNUM = 100_000_000  # aka x (largest number in dataset)

#######################################################################################################

#
# part 3: plot number of key comparisons over diff input size, for both insertion sort and merge sort
# once insertion sort and merge sort graph intersect that should be the S
#

# arraySize = 1  # reset array size
# comparisonsList3 = {'arraySize': [], 'insertion sort comp': [] , 'merge sort comp': []}

# while arraySize <= MAXARRAYSIZE:

#     randomIntegers = random.randint(1, LARGESTNUM, arraySize)
#     randomIntegers2 = randomIntegers.copy () 

#     numComparisonsInsert = insertionSort(randomIntegers)
#     numComparisonsMerge = mergeSortOriginal(randomIntegers2)

#     comparisonsList3['arraySize'].append(arraySize)
#     comparisonsList3['insertion sort comp'].append (numComparisonsInsert)
#     comparisonsList3['merge sort comp'].append (numComparisonsMerge)

#     arraySize += 1

# df = pd.DataFrame(comparisonsList3)
# df.plot(x='arraySize' , y = ['insertion sort comp' , 'merge sort comp'] , kind='line')
# plt.show()
