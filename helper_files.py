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
        fitness = sorted(fitness, reverse=False)

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

def plot_blocks(blocks):
    fig, ax = plt.subplots()
    x = y = 0
    height = 0.5
    cmap = cm.Paired
    for i, block in enumerate(blocks):
        rect = plt.Rectangle((x, y), block, height, alpha=0.5, color=cmap(i))
        ax.text(x + block / 2, 0.25, f'{i}', horizontalalignment='center', verticalalignment='center', fontsize=30,
                color='black')
        x += block + 10
        ax.add_patch(rect)

    plt.xlim(0, x)
    ax.axis('off')
    plt.show()

def plot_cross_over(parents, children, crossover_point, blocks, max_length):
    fig, ax = plt.subplots(figsize=(10,7))
    height = 7.5
    cmap = cm.Paired
    y = 0
    xmax = 0
    text_shift = 40
    x_spacing = 10
    x_0 = 0

    arrow_points = []
    x_crossover = -1

    x = x_0
    color_dict = {0: "r", 1: "b"}
    for j, child in enumerate(children):
        ax.text(x , y + height/2, f'Child {j+1}:', horizontalalignment='left', verticalalignment='center',fontsize=20, color=color_dict[j])
        x += text_shift
        x_old = x
        for i, chosen in enumerate(child):
            if i == crossover_point:
                x_ = x-1
                y_ = y-height*0.25
                rect = plt.Rectangle((x_,y_), 2, height*1.5, color='black')
                ax.add_patch(rect)
                x_crossover = x_
                arrow_points.append(((x_crossover-x_old)/2+x_old, y_+height*1.5))

            if chosen == 1:
                rect = plt.Rectangle((x, y), blocks[i], height, alpha=0.5, color=cmap(i))
                ax.text(x + blocks[i] / 2, y + height/2, f'{i}', horizontalalignment='center', verticalalignment='center',fontsize=20, color='black')
                x += blocks[i]
                if x > xmax:
                    xmax = x
                ax.add_patch(rect)

        arrow_points.append(((x_crossover-x)/2+x, y_+height*1.5))
        x += x_spacing


    x = x_0
    y += height*3
    name_dict = {0: "a", 1: "b"}
    for j, parent in enumerate(parents):
        ax.text(x , y + height/2, f'Parent {name_dict[j]}:', horizontalalignment='left', verticalalignment='center',fontsize=20, color='black')
        x += text_shift
        x_old = x
        for i, chosen in enumerate(parent):
            if i == crossover_point:
                x_ = x-1
                y_ = y-height*0.25
                rect = plt.Rectangle((x_,y_), 2, height*1.5, color='black')
                ax.add_patch(rect)
                x_crossover = x_
                arrow_points.append(((x_crossover-x_old)/2+x_old, y_))

            if chosen == 1:
                rect = plt.Rectangle((x, y), blocks[i], height, alpha=0.5, color=cmap(i))
                ax.text(x + blocks[i] / 2, y + height/2, f'{i}', horizontalalignment='center', verticalalignment='center',fontsize=20, color='black')
                x += blocks[i]
                if x > xmax:
                    xmax = x
                ax.add_patch(rect)
        arrow_points.append(((x_crossover-x)/2+x, y_))
        x += x_spacing

    y += height*2

    ax.annotate("", xy=(arrow_points[4][0], arrow_points[4][1]), xytext=(arrow_points[0][0], arrow_points[0][1]),arrowprops=dict(arrowstyle="<-", color=color_dict[0]))
    ax.annotate("", xy=(arrow_points[7][0], arrow_points[7][1]), xytext=(arrow_points[1][0], arrow_points[1][1]),arrowprops=dict(arrowstyle="<-", color=color_dict[0]))
    ax.annotate("", xy=(arrow_points[5][0], arrow_points[5][1]), xytext=(arrow_points[3][0], arrow_points[3][1]),arrowprops=dict(arrowstyle="<-", color=color_dict[1]))
    ax.annotate("", xy=(arrow_points[6][0], arrow_points[6][1]), xytext=(arrow_points[2][0], arrow_points[2][1]),arrowprops=dict(arrowstyle="<-", color=color_dict[1]))


    plt.xlim(0, np.max([max_length+x_0, xmax]))
    plt.ylim(-10, y )
    ax.axis('off')


def plot_mutation(vorher, nacher, blocks, height):

    cmap = cm.Paired
    fig, ax = plt.subplots(figsize=(10,7))
    x=0
    y=0
    xmax = 0
    text_shift = 60

    ax.text(x , y + height/2, f'Vor Mutatation:', horizontalalignment='left', verticalalignment='center',fontsize=20, color='black')
    x += text_shift
    for i, chosen in enumerate(vorher):
        if chosen == 1:
            rect = plt.Rectangle((x, y), blocks[i], height, alpha=0.5, color=cmap(i))
            ax.text(x + blocks[i] / 2, y + height/2, f'{i}', horizontalalignment='center', verticalalignment='center',fontsize=20, color='black')
            x += blocks[i]
            if x > xmax:
                xmax = x
            ax.add_patch(rect)


    x=0
    y -= height*2
    ax.text(x , y + height/2, f'Nach Mutatation:', horizontalalignment='left', verticalalignment='center',fontsize=20, color='black')
    x += text_shift
    for i, chosen in enumerate(nacher):
        if chosen == 1:
            rect = plt.Rectangle((x, y), blocks[i], height, alpha=0.5, color=cmap(i))
            ax.text(x + blocks[i] / 2, y + height/2, f'{i}', horizontalalignment='center', verticalalignment='center',fontsize=20, color='black')
            x += blocks[i]
            if x > xmax:
                xmax = x
            ax.add_patch(rect)
    y -= height*2

    plt.xlim(0, xmax)
    plt.ylim(y, height)
    ax.axis('off')
    plt.show()


def plot_fitness(fitness_values):
    fig, ax = plt.subplots()
    ax.plot(fitness_values)
    ax.set_xlabel('Generation', fontsize=20)
    ax.set_ylabel('Fitness', fontsize=20)
    ax.set_xlim(0, None)
    ax.set_ylim(0,1)
    plt.tick_params(axis='both', which='major', labelsize=18)

if __name__ == '__main__':
    pass