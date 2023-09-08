sakana~

last updated 8/9/23

compOverSize.py: part ci <br>
create a CSV file with column 1 as the arraySize (1000 to MAXARRAYSIZE), and remaining columns as number of key comparisons needed for different S (0 to 30) <br>
for each row the randomIntegers array used for sorting is the same (ie a new randomIntegers array is only generated for each array size) <br>
todo: plot a line graph for each different value of S on excel <br>

compOverS.py: part cii <br>
fix arraySize as 1 million, create a CSV file with column 1 as S (0 to 40), and remaining columns as the number of key comparisons needed for different randomly generated list <br>
for each column the randomIntegers array is the same (ie as S varies the randomIntegers array used for sorting is the same) <br>
todo: create an average key comparisons column in excel and plot a graph from that <br>

originalHyrbod.py: part d <br>
compare the number of key comparisons and CPU times between original merge sort and hybrid merge sort <br>

sorting.py: sorting functions<br>

main.py and globalData.py is no longer used. Now each script stores its own global data (more convenient this way)<br>


