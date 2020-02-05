
#%%
# 1. Import numpy as np and see the version
import numpy as np
print(np.__version__)

# %%
# 2. How to create a 1D array?
import numpy as np
arr = np.arange(10)
print(arr)

# %%
# 3. How to create a boolean array?
import numpy as np
arr = np.ones((3,3), dtype=bool)
arr1 = np.full((3,3),False,dtype=bool)
print(arr,arr1,sep="\n")

# %%
# 4. How to extract items that satisfy a given condition from 1D array?
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr % 2 == 1])

# %%
# 5. How to replace items that satisfy a condition with another value in numpy array?
import numpy as np
arr[arr % 2 == 1] = -1
print(arr)

# %%
# 6. How to replace items that satisfy a condition without affecting the original array?
import numpy as np
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr,out,sep="\n")


# %%
# 7. How to reshape an array?
arr = np.arange(10)
print(arr.reshape(2, -1) )


# %%
# 8. How to stack two arrays vertically?
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(np.concatenate([a, b], axis=0))
print(np.vstack([a, b]))
print(np.r_[a, b])

# %%
# 9. How to stack two arrays horizontally?
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(np.concatenate([a, b], axis=1))
print(np.hstack([a, b]))
print(np.c_[a, b])


# %%
# 10. How to generate custom sequences in numpy without hardcoding?
a = np.array([1,2,3])
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])


# %%
# 11 Generating visualizations with pyplot is very quick
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4,5])
plt.ylabel('some numbers')
plt.show()


# %%
# 12 plot x and y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


# %%
# 13 plot using x and y and circle point
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()


# %%
# 14 evenly sampled time at 200ms intervals
# # red dashes, blue squares and green triangles
import numpy as np
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# %%
# 15 Plotting with MARKER SIZE AND COLOR keyword strings
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')   
plt.show()


# %%
# 16 Plotting with categorical variables
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()


# %%
# 17 Working with multiple figures and axes
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


# %%
# 18 Working with text
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


# %%
# 19 Annotating text
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
plt.ylim(-2, 2)
plt.show()



# %%
# 20 Logarithmic and other nonlinear axes
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()

# %%
