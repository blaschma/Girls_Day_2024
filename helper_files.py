import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from IPython.display import display, HTML
import pandas as pd


cmap = cm.tab20b

def plot_population(population, blocks, max_length, fitness=None, sort=False, with_fitness=False):
    fig, ax = plt.subplots(figsize=(10,7))

    height = 7.5

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

    plt.axvline(x_0, ls='--', color='red')
    plt.axvline(x_0+max_length, ls='--', color='red')

    plt.xlim(0, np.max([max_length+x_0, xmax]))
    plt.ylim(0, y)
    ax.axis('off')

def plot_blocks(blocks):
    fig, ax = plt.subplots(figsize=(10,3))
    x = y = 0
    height = 0.25
    for i, block in enumerate(blocks):
        rect = plt.Rectangle((x, y), block*4, height, alpha=0.5, color=cmap(i))
        ax.text(x + block*2, height/2, f'{i}', horizontalalignment='center', verticalalignment='center', fontsize=20,
                color='black')
        x += block + 60
        ax.add_patch(rect)

    plt.xlim(0, x)
    plt.ylim(0, height)
    ax.axis('off')
    plt.show()

def plot_cross_over(parents, children, crossover_point, blocks, max_length):
    fig, ax = plt.subplots(figsize=(10,7))
    height = 7.5
    y = 0
    xmax = 0
    text_shift = 75
    x_spacing = 20
    x_0 = 0

    arrow_points = []
    x_crossover = -1

    x = x_0
    color_dict = {0: "r", 1: "b"}
    for j, child in enumerate(children):
        ax.text(x , y + height/2, f'Kind {j+1}:', horizontalalignment='left', verticalalignment='center',fontsize=20, color=color_dict[j])
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
        ax.text(x , y + height/2, f'Elternteil {name_dict[j]}:', horizontalalignment='left', verticalalignment='center',fontsize=20, color='black')
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
    plt.ylim(-5, y )
    ax.axis('off')


def plot_mutation(vorher, nacher, blocks, height):

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

    plt.xlim(0, xmax)
    plt.ylim(y, height)
    ax.axis('off')
    plt.show()


def plot_fitness(fitness_values):
    fig, ax = plt.subplots()
    ax.plot(fitness_values, marker="x", lw = 3, markersize=10)
    ax.set_xlabel('Generation', fontsize=20)
    ax.set_ylabel('Fitness', fontsize=20)
    ax.set_xlim(0, None)
    ax.set_ylim(0,1)
    plt.tick_params(axis='both', which='major', labelsize=18)

def print_population(population, blocks, col_prefix="Individuum", row_names=None):
    #print population in a table
    population = population[::-1]
    col_names = [f"Block {i}" for i in range(len(blocks))]
    index = np.arange(0, len(population))
    if row_names is None:
        row_names = [f"{col_prefix} {i}" for i in range(len(population))]
        #row_names = sorted(row_names, reverse=False)



    df = pd.DataFrame(population, columns=col_names, index=row_names)
    # Sort DataFrame by row names
    #df = df.reindex(row_names)
    styled_df = df.style.apply(lambda x: ['background: lightgray' if i % 2 == 0 else 'background: white' for i in range(len(x))], axis=1)
    # Define CSS styles for borders
    styles = [
    dict(selector="th", props=[("border", "1px solid black")]),
    dict(selector="td", props=[("border", "1px solid black")]),
    ]
    styled_df.set_table_styles(styles)
    display(HTML(styled_df.render()))

def create_nice_example(population, fitness, max_width, blocks):
    """
    This function creates a nice example for the population. It is obviously not the best solution, but a simple one.
    :param population:
    :return:
    """
    def calc_fitness(individuum):
        length = 0
        for i, chosen in enumerate(individuum):
            if chosen == 1:
                length += blocks[i]
        if length > max_width:
            return 0
        else:
            return length / max_width

    for i, individuum in enumerate(population):
        n = 3
        if fitness[i] > 0.65:
            #set n entries of individuum from 1 to 0. make sure that entries are 1 in the beginning
            for j in range(0, n):
                if individuum[j] == 1:
                    individuum[j] = 0
            fitness[i] = calc_fitness(individuum)

def correct_blocks(blocks, max_width):
    sum = np.sum(blocks)
    while sum < max_width:
        blocks = [width*1.1 for width in blocks]
        sum = np.sum(blocks)
    return blocks

if __name__ == '__main__':
    pass