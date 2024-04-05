import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def plot_population(population, blocks, max_length, fitness=None, sort=False, with_fitness=False):
    fig, ax = plt.subplots(figsize=(10,7))

    height = 7.5
    cmap = cm.Paired
    y = 0
    xmax = 0

    if with_fitness:
        x_0 = 30
    else:
        x_0 = 0

    if sort:
        #fitness = [calc_fitness(individuum) for individuum in population]
        population = [x for _, x in sorted(zip(fitness, population), key=lambda pair: pair[0], reverse=False)]

    for i, individuum in enumerate(population):
        x = x_0
        if with_fitness:
            #fitness = calc_fitness(individuum)
            ax.text(0 , y + height/2, f'f={fitness[i]:.2f}', horizontalalignment='left', verticalalignment='center',fontsize=20, color='black')
        for i, chosen in enumerate(individuum):
            if chosen == 1:
                rect = plt.Rectangle((x, y), blocks[i], height, alpha=0.5, color=cmap(i))
                ax.text(x + blocks[i] / 2, y + height/2, f'{i}', horizontalalignment='center', verticalalignment='center',fontsize=20, color='black')
                x += blocks[i]
                if x > xmax:
                    xmax = x
                ax.add_patch(rect)
        y += height*2

    plt.axvline(x_0, ls='--', color='black')
    plt.axvline(x_0+max_length, ls='--', color='black')

    plt.xlim(0, np.max([max_length+x_0, xmax]))
    plt.ylim(0, y)
    ax.axis('off')



if __name__ == '__main__':
    pass