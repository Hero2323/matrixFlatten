# matrixFlatten

3D Matrix Flatten algorithm

# How it works
Let's first start of with a 2D matrix ```Q``` [n x m] (where n is the number of rows and m is the number of columns). to be flattened we'll need a 1D matrix ```L``` of length n * m. 

We know that: ```Q[0, 0] = L[0]``` and that ```Q[0, 1] = L[1]``` and that ```Q[0, m - 1] = L[m - 1]``` and that ```Q[1, 0] = L[m]``` and that ```Q[1, 1] = L[m + 1]```. 

From the above the we can conclude that every time we move from a row to another row, we jump m (the number of elements in a single row) elements.

So, the equation for 2D matrix flattening would be (assuming indexing using i, j for the 2D matrix and y for the 1D matrix): ```y = j + i * m```.

This can be generalized for 3D matrix flattening where the 3D matrix Q [n x m x p] is to be flattened to L of length q = n * m * p.

We know that ```Q[1, 1, 0] = L[m + 1]``` and that ```Q[n - 1, m - 1, 0] = L[m - 1 + (n - 1) * m] = L[nm - 1]```, So ```Q[0, 0, 1] = L[nm]``` and ```Q[0, 1, 1] = L[nm + 1]```.  

From the above, it can be concluded that every time we jump 1 plane (from k = 0 to k = 1 for example), we jump nm elements

So, the equation for 3D matrix flattening would be (assuming indexing using i, j, k for the 3D matrix and y for the 1D matrix: ```y = j + i * m + k * n * m```).
