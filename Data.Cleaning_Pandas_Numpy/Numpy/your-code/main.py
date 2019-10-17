#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

#a = np.ones([2,3,5])
a = np.random.random((2,3,5))


#4. Print a.

print(a)

#5. Create a 5x3x2 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

#b = np.ones([5,3,2])
b = np.full((5,3,2),1)

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size)
print(b.size)

    #yes they do, they are both 30 


#8. Are you able to add a and b? Why or why not?


#No they aren't the same shape. 

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a,c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)

# [[[0.91017954 0.57478906 0.94407062 0.8625837  0.6562442 ]
#   [0.39054745 0.9017394  0.10355549 0.34045436 0.02423269]
#   [0.55827331 0.39615092 0.54569641 0.50928094 0.20177063]]

#  [[0.63438925 0.28242037 0.07109316 0.12818604 0.25005389]
#   [0.62285351 0.56668885 0.15840444 0.39342135 0.29821441]
#   [0.39311996 0.0019783  0.98673559 0.5191495  0.59586619]]]

print(d)

# [[[1.91017954 1.57478906 1.94407062 1.8625837  1.6562442 ]
#   [1.39054745 1.9017394  1.10355549 1.34045436 1.02423269]
#   [1.55827331 1.39615092 1.54569641 1.50928094 1.20177063]]

#  [[1.63438925 1.28242037 1.07109316 1.12818604 1.25005389]
#   [1.62285351 1.56668885 1.15840444 1.39342135 1.29821441]
#   [1.39311996 1.0019783  1.98673559 1.5191495  1.59586619]]]

# This size of the arrays are the same, but the second array is array a + array b so that is why the values are + 1

#12. Multiply a and c. Assign the result to e.

e = np.multiply(a,c)

#13. Does e equal to a? Why or why not?

# E and a are both equal. They are the exact same matrix. 


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_mean = np.mean(d)

1.4981327887972689

d_max = np.max(d)

1.9727925081629603

d_min = np.min(d)

1.0242839558393713

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.zeros([2,3,5])



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.If a value equals to d_mean, assign 50 to the corresponding value in f.Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for a in range(len(d)):
    for i in range(len(d[a])):
        for j in range(len(d[a][i])):
            if d[a][i][j] > d_min and d[a][i][j] < d_mean:
                f[a][i][j] = 25
            elif d[a][i][j] > d_mean and d[a][i][j] < d_max:
                f[a][i][j] = 75
            elif d[a][i][j] == d_mean:
                f[a][i][j] = 50
            elif d[a][i][j] == d_min:
                f[a][i][j] = 0
            elif d[a][i][j] == d_max:
                f[a][i][j] = 100




# #17. Print d and f. Do you have your expected f?


print(d)
print(f)

#Yes I have the correct expected value for f. They are printed below.

"""
d
[[[1.03417993 1.96410461 1.89701853 1.68587593 1.75444061]
  [1.77167905 1.56113095 1.99312875 1.77842559 1.91527643]
  [1.24793608 1.14723093 1.49228044 1.21958937 1.20979877]]

 [[1.56162478 1.87980589 1.2221157  1.94868763 1.60077371]
  [1.47436511 1.05972495 1.74804196 1.91939737 1.47082823]
  [1.78730863 1.80281217 1.79861798 1.13473347 1.62288594]]]

f
[[[  0.  75.  75.  75.  75.]
  [ 75.  25. 100.  75.  75.]
  [ 25.  25.  25.  25.  25.]]

 [[ 25.  75.  25.  75.  75.]
  [ 25.  25.  75.  75.  25.]
  [ 75.  75.  75.  25.  75.]]]
"""



#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
#first you have to recreate f with empty strings so you can populate the array with strings

f = np.full([2,3,5],"")

#then just change assignments int he conditionals to the strings you want

for a in range(len(d)):
    for i in range(len(d[a])):
        for j in range(len(d[a,i])):
            if d[a][i][j] > d_min and d[a][i][j] < d_mean:
                f[a][i][j] = 'B'
            elif d[a][i][j] > d_mean and d[a][i][j] < d_max:
                f[a][i][j] = 'D'
            elif d[a][i][j] == d_mean:
                f[a][i][j] = 'C'
            elif d[a][i][j] == d_min:
                f[a][i][j] = 'A'
            elif d[a][i][j] == d_max:
                f[a][i][j] = 'E'
                
"""
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""