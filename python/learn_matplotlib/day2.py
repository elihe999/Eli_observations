import matplotlib.pyplot as plt 
fig = plt.figure()
x= range(10)
y= range(10)
#color
#plt.plot(x, y, 'red')
#width
#plt.plot(x, y, 'red', linewidth = '10')
#label
#plt.plot(x, y, 'red', linewidth = '1', label="example")
#marker linestyle
plt.plot(x, y, 'red', linewidth = '1', label="example", marker = '.', linestyle=":")

plt.legend()
plt.show()