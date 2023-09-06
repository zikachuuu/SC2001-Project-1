from numpy import random
import os
import time
import sorting
from globalData import MAXARRAYSIZE , LARGESTNUM

scriptPath = os.path.dirname(__file__)

#
# part d: compare the number of key comparisons and CPU times between original merge sort and hybrid merge sort
#

S = int(input("Choose S: ")) # thereshold for size of subarray (switch from insertionSort to mergeSort)
print()

randomIntegers = random.randint(1, LARGESTNUM, MAXARRAYSIZE).tolist()
randomIntegers2 = randomIntegers.copy()

start = time.time()
keyComparisons = sorting.mergeSortOriginal (randomIntegers)
end = time.time()

print ("Original Merge Sort:")
print ("Key Comparisons:" , keyComparisons)
print ("CPU Time:" , end - start , "seconds")
print()

start = time.time()
keyComparisons = sorting.mergeSortHybrid(randomIntegers2 , S)
end = time.time()

print("Hybrid Merge Sort:")
print("Key Comparisons:", keyComparisons)
print("CPU Time:", end - start, "seconds")




