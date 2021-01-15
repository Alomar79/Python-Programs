import matplotlib.pyplot as plt

a = [-4,-3,-2,-1,0,1,2,3,4]
b = list(range(7))

plt.plot(a)
plt.plot(b)

# generate axes lables
plt.ylabel('Parallel Lines Plot')
plt.xlabel('Integer Range')

# display plot
plt.show()

