# -*- coding: utf-8 -*-
#%%

# exceptions
x = 10
zero = 0

try:
    divide = x/zero
except ZeroDivisionError:
    x = 0
print(x)

#%%

try:
    1/0
except:
    print("except")
else:
    print("else")
finally:
    print("done")

#%%

# index error
list1 = [1,2,3,4]
print(list1[15])

# module not found error
import numpyy

# file not found error
import pandas as pd
pd.read_csv("a.txt")

# a type error
"2" + 2

# value error
int("xxx")