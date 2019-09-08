# String compare

This program reads all the files inside a directory as text and then compares then as text using some distance libraries then show a matrix that indicates the the similarity between each file content.

## Prerequisites

This programs runs with python 3.5.

Install these libraries first before running the program:

### Numpy

```
conda install -c anaconda numpy
OR
pip install numpy
```

### fuzzywuzzy

```
conda install -c conda-forge fuzzywuzzy
Or
pip install fuzzywuzzy
```

### terminaltables

```
conda install -c binstar terminaltables
OR
pip install terminaltables
```

### StringDist

```
pip install StringDist
```

## Sample input

```
Python main.py C:\test
```

## Sample output

```
+-------+-------+-------+-------+-------+-------+-------+
|       | 1.txt | 2.txt | 3.txt | 4.txt | 5.txt | 6.txt |
+-------+-------+-------+-------+-------+-------+-------+
| 1.txt | 0.0   | 22.0  | 67.0  | 77.0  | 15.0  | 22.0  |
| 2.txt | 22.0  | 0.0   | 43.0  | 33.0  | 67.0  | 100.0 |
| 3.txt | 67.0  | 43.0  | 0.0   | 89.0  | 33.0  | 43.0  |
| 4.txt | 77.0  | 33.0  | 89.0  | 0.0   | 25.0  | 33.0  |
| 5.txt | 15.0  | 67.0  | 33.0  | 25.0  | 0.0   | 67.0  |
| 6.txt | 22.0  | 100.0 | 43.0  | 33.0  | 67.0  | 0.0   |
+-------+-------+-------+-------+-------+-------+-------+
```



<br><br>
<br><br>
This program was made by [Mahmoud Badry](mailto:mma18@fayoum.edu.eg) @2017