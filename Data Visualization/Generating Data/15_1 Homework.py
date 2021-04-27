from matplotlib import pyplot as plt


x_values = list(range(5001))#list of values to be cubed
#cubes = [1, 8, 27, 64, 125] #cubes of x_values
cubes = [x**3 for x in x_values] #finding the cubes of the x-values



plt.style.use ("seaborn")

fig, ax = plt.subplots()

ax.scatter(x_values, cubes, c= cubes, cmap = plt.cm.Greens, s = 10)

ax.set_title ("Cubes", fontsize = 24)
ax.set_xlabel ("Value", fontsize = 14)
ax.set_ylabel ("Cube of Value", fontsize = 14)

ax.tick_params(axis = "both", labelsize =14)

ax.axis ([0, 5100, 0, 5100 ** 3])###

plt.show()
