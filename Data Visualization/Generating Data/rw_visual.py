import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use ("classic")
    fig, ax = plt.subplots()
    
    point_numbers = range(rw.num_points)
    
    ax.scatter (rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues,
                edgecolors = "none", s = 15)



    
    #ax.scatter(rw.x_values, rw.y_values, s = 15)
    plt.show()


    keep_running = input("Make another plot? (y/n):")
    if keep_running == "n":
        break
