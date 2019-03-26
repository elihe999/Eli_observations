import matplotlib.pyplot as plt
fig = plt.figure()

list_a = range(10)
list_b = [23, 34, 54, 23, 43, 23, 63, 23, 56, 76]
plotdict = {'x': list_a, 'y': list_b}

plt.plot('x', 'y', 'bD-', data=plotdict, linewidth = '1', label="example", marker = '.', linestyle=":")

plt.legend()
plt.show()