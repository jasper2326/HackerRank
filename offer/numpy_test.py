# -*- coding:utf-8 -*-
# 1.
import numpy as np
print(np.__version__)

# 2.
a = np.arange(10)
print(a)

# 3.
b = np.ones((3, 3), dtype=bool)
print(b)

# 4.
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr % 2 == 1])

# 5.
arr[arr % 2 == 1] = -1
print(arr)

# 6.
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(out, arr)

# 7.
arr = np.arange(10)
print(arr.reshape([2, -1]))

# 8.
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(np.vstack([a, b]))

# 9.
print(np.hstack([a, b]))

# 10.
a = np.array([1, 2, 3])
print(np.r_[np.repeat(a, 3)], np.r_[np.tile(a, 3)])

# 11.
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a, b))

# 12.
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print(np.setdiff1d(a, b))

# 13.
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.where(a == b))

# 14.
a = np.arange(15)
index = np.where((a >= 5) & (a <= 10))
print(a[index])
print(a[(a >= 5) & (a <= 10)])

# 15.
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(pair_max(a, b))

# 16.
arr = np.arange(9).reshape(3,3)
print(arr[:, [1, 0, 2]])

# 17.
arr = np.arange(9).reshape(3, 3)
print(arr)
print(arr[[1, 0, 2], :])

# 18.
arr = np.arange(9).reshape(3, 3)
print(arr[::-1])

# 19.
arr = np.arange(9).reshape(3, 3)
print(arr[:, ::-1])

# 20.
rand_arr = np.random.uniform(5, 10, size=(5, 3))
print(rand_arr)

# 21.
rand_arr = np.random.random((5,3))
np.set_printoptions(precision=3)
print(rand_arr[:4])

# 22.
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
#print(rand_arr)
np.set_printoptions(suppress=False)
np.set_printoptions(suppress=True, precision=6)  # precision is optional
print(rand_arr)

# 23.
a = np.arange(15)
np.set_printoptions(threshold=6)
a = np.arange(15)
print(a)

# 24.
np.set_printoptions(threshold=6)
a = np.arange(15)
np.set_printoptions(threshold=np.nan)
print(a)

# 25.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris[:3])

# 26.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
print(iris_1d.shape)
species = np.array([row[4] for row in iris_1d])
print(species[:5])

# 27.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)

iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
print(iris_2d[:4])

# 28.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
print(sepallength)
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
print(mu, med, sd)

# 29.
Smax, Smin = sepallength.max(), sepallength.min()
S = (sepallength - Smin)/(Smax - Smin)
print(S)

# 30.
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

print(softmax(sepallength))

# 31.
print(np.percentile(sepallength, [5, 95]))

# 32.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')

i, j = np.where(iris_2d)
np.random.seed(100)
iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan
print(iris_2d)

# 33.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

print("Number of missing values: \n", np.isnan(iris_2d[:, 0]).sum())
print("Position of missing values: \n", np.where(np.isnan(iris_2d[:, 0])))

# 34.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
print(iris_2d[condition])

# 35.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

any_nan_in_row = np.array([~np.any(np.isnan(row)) for row in iris_2d])
print(iris_2d[any_nan_in_row])

# 36.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print(np.corrcoef(iris[:, 0], iris[:, 1]))

# 37.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

print(np.isnan(iris_2d).any())

# 38.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

iris_2d[np.isnan(iris_2d)] = 0
print(iris_2d[:4])

# 39. url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
species = np.array([row.tolist()[4] for row in iris])
#print(species)

print(np.unique(species, return_counts=True))

# 40.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
petal_length_bin = np.digitize(iris[:, 2].astype('float'), [0, 3, 5, 10])

label_map = {1: 'small', 2: 'medium', 3: 'large', 4: np.nan}
petal_length_cat = [label_map[x] for x in petal_length_bin]
print(petal_length_cat)

# 41.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')

# Solution
# Compute volume
sepallength = iris_2d[:, 0].astype('float')
petallength = iris_2d[:, 2].astype('float')
volume = (np.pi * petallength * (sepallength**2))/3

# Introduce new dimension to match iris_2d's
volume = volume[:, np.newaxis]

# Add the new column
out = np.hstack([iris_2d, volume])
print(out)

# 42.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, 4]
np.random.seed(100)
probs = np.r_[np.linspace(0, 0.500, num=50), np.linspace(0.501, .750, num=50), np.linspace(.751, 1.0, num=50)]
index = np.searchsorted(probs, np.random.random(150))
species_out = species[index]
print(np.unique(species_out, return_counts=True))

# 43.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

petal_len_setosa = iris[iris[:, 4] == b'Iris-setosa', [2]].astype('float')
print(np.unique(np.sort(petal_len_setosa))[-2])

# 44.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

print(iris[iris[:, 0].argsort()])

# 45.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

vals, counts = np.unique(iris[:, 3], return_counts=True)
print(vals[np.argmax(counts)])

# 46.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

print(np.argmax(iris[:, 3].astype('float') > 1.0))

# 47.
np.set_printoptions(precision=2)
np.random.seed(100)
a = np.random.uniform(1,50, 20)

print(np.clip(a, a_min=10, a_max=30))

# 48.
np.random.seed(100)
a = np.random.uniform(1,50, 20)

print(a.argsort()[-5:])
print(a[a.argsort()[-5:]])

# 49.
np.random.seed(100)
arr = np.random.randint(1, 11, size=(6, 10))
print(arr)

# 50.
def counts_of_all_values_rowwise(arr2d):
    # Unique values and its counts row wise
    num_counts_array = [np.unique(row, return_counts=True) for row in arr2d]

    # Counts of all values row wise
    return([[int(b[a==i]) if i in a else 0 for i in np.unique(arr2d)] for a, b in num_counts_array])

# Print
print(np.arange(1,11))
print(counts_of_all_values_rowwise(arr))

# 51.
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)

array_of_arrays = np.array([arr1, arr2, arr3])
print('array_of_arrays: ', array_of_arrays)

arr_2d = np.concatenate(array_of_arrays)
print(arr_2d)

# 52.
np.random.seed(101)
arr = np.random.randint(1,4, size=6)
print(arr)

# Solution:
def one_hot_encodings(arr):
    uniqs = np.unique(arr)
    out = np.zeros((arr.shape[0], uniqs.shape[0]))
    for i, k in enumerate(arr):
        out[i, k-1] = 1
    return out

print(one_hot_encodings(arr))

# 53.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
species = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)
np.random.seed(100)
species_small = np.sort(np.random.choice(species, size=20))
print(species_small)

print([i for val in np.unique(species_small) for i, grp in enumerate(species_small[species_small==val])])

# 54.
np.random.seed(10)
a = np.random.randint(20, size=10)
print('Array: ', a)

# Solution
print(a.argsort().argsort())
print('Array: ', a)

# 55.
np.random.seed(10)
a = np.random.randint(20, size=[2, 5])
print(a)

# Solution
print(a.ravel().argsort().argsort().reshape(a.shape))

# 56.
np.random.seed(100)
a = np.random.randint(1,10, [5,3])
print(a)

print(np.amax(a, axis=1))

# 57.
np.random.seed(100)
a = np.random.randint(1,10, [5,3])
print(a)

print(np.apply_along_axis(lambda x: np.min(x)/np.max(x), arr=a, axis=1))

# 58.
np.random.seed(100)
a = np.random.randint(0, 5, 10)
print('Array: ', a)

out = np.full(a.shape[0], True)

# Find the index positions of unique elements
unique_positions = np.unique(a, return_index=True)[1]

# Mark those positions as False
out[unique_positions] = False
print(out)

# 59.
rl = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

numeric_column = iris[:, 1].astype('float')  # sepalwidth
grouping_column = iris[:, 4]  # species

a = [[group_val, numeric_column[grouping_column==group_val].mean()] for group_val in np.unique(grouping_column)]
print(a)

# 60.
from io import BytesIO
from PIL import Image
import PIL, requests

# Import image from URL
URL = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response = requests.get(URL)

# Read it as Image
I = Image.open(BytesIO(response.content))

# Optionally resize
#I = I.resize([150,150])

# Convert to numpy array
arr = np.asarray(I)

# Optionaly Convert it back to an image and show
im = PIL.Image.fromarray(np.uint8(arr))
#Image.Image.show(im)

# 61.
a = np.array([1,2,3,np.nan,5,6,7,np.nan])
print(a[~np.isnan(a)])

# 62.
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8])
#print(np.linalg.norm(a - b))

# 63.
a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
doublediff = np.diff(np.sign(np.diff(a))) # er jie dao shu
peak_locations = np.where(doublediff == -2)[0] + 1
peak_locations
print(doublediff)

# 64.
a_2d = np.array([[3,3,3],[4,4,4],[5,5,5]])
b_1d = np.array([1,2,3])

# Solution
print(a_2d - b_1d[:,None])

# 65.
x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n = 5

# Solution 1: List comprehension
print([i for i, v in enumerate(x) if v == 1][n-1])

# 66.
dt64 = np.datetime64('2018-02-25 22:10:10')

# Solution
from datetime import datetime
print(dt64.astype(datetime))

# 67.
def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

# 68.
length = 10
start = 5
step = 3

def seq(start, length, step):
    end = start + (step*length)
    return np.arange(start, end, step)

seq(start, length, step)

# 69.
dates = np.arange(np.datetime64('2018-02-01'), np.datetime64('2018-02-25'), 2)
print(dates)

filled_in = np.array([np.arange(date, (date+d)) for date, d in zip(dates, np.diff(dates))]).reshape(-1)

# add the last day
output = np.hstack([filled_in, dates[-1]])
print(output)

# 70.
def gen_strides(arr, stride_len=5, window_len=5):
    n_strides = ((a.size-window_len)//stride_len) + 1
    # return np.array([a[s:(s+window_len)] for s in np.arange(0, a.size, stride_len)[:n_strides]])
    return np.array([a[s:(s+window_len)] for s in np.arange(0, n_strides*stride_len, stride_len)])

print(gen_strides(np.arange(15), stride_len=2, window_len=4))




