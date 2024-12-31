from numpy import *

Arr1 = array([1,8,3,5,9])
Arr2 = array([2,7,4,6,10])

Ans = Arr1.copy()

for i in range(len(Arr1)):
    Ans[i] += Arr2[i]

print(Ans)


