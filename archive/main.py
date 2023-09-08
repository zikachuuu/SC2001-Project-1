# from numpy import random
# import time
# import pandas as pd
# import matplotlib.pyplot as plt
# import os
# import re

# scriptPath = os.path.dirname(__file__)

# def partCi():
#     for fileName in os.listdir(f"{scriptPath}\\result"):
#         if fileName[:14] == "compOverSize_S":
#             print(fileName)
#             df = pd.read_csv(f"{scriptPath}\\result\\{fileName}")

#             x = df['arraySize']
#             y = df['keyComparisons']
#             S = re.findall('\d+', fileName)[0]
#             plt.plot(x , y , label=f"S = {S}")

#     plt.legend(loc="upper left" , numpoints=1)
#     plt.xlabel ("Array Size")
#     plt.ylabel ("Number of Key Comparisons")
#     plt.show()


# print ("1. (part ci) Plot the number of key comparisons over different sizes of the input list n, using the created compOverSize_SX.csv files in result folder")
# print ("2. (coming soon) (part cii) Plot the number of key comaprisons over different values of S, using the created compOverS_arraySizeX.csv files in result folder")
# choice = int(input ("Enter your choice: "))

# if choice == 1 :
#     print ("1. Create a graph using all compOverSize_SX.csv files")
#     print ("2. (coming soon) Create a graph using selected compOverSize_SX.csv files")
#     choice = int (input ("Enter your choice: "))

#     if (choice == 1) :
#         partCi()
#     else :
#         pass
# else :
#     pass




        

    

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
