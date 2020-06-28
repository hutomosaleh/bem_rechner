import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatch


def newline(point_1, point_2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if point_2[0] == point_1[0]:
        xmin = xmax = point_1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = point_1[1] + (point_2[1] - point_1[1]) / (point_2[0] - point_1[0]) * (xmax - point_1[0])
        ymin = point_1[1] + (point_2[1] - point_1[1]) / (point_2[0] - point_1[0]) * (xmin - point_1[0])

    l = mlines.Line2D([xmin, xmax], [ymin, ymax])
    ax.add_line(l)
    return l


def add_annotation(annotation, shape_object, axes):
    axes.add_artist(shape_object)
    rx, ry = shape_object.get_xy()
    cx = rx + shape_object.get_width() / 2.0
    cy = ry + shape_object.get_height() / 2.0

    axes.annotate(annotation, (cx, cy), color='black',
                  fontsize=10, ha='center', va='center')


def reverse_dict(dictionary):
    for key in dictionary.keys():
        if "-" in dictionary[key][1]:
            dictionary[key][1] = dictionary[key][1].replace("-", " ")
        else:
            dictionary[key][1] = dictionary[key][1].replace(" ", "-")
    return dictionary


def plot_wicklungsplan(nut, schicht=1, intv=2, y_y0=0, vers=False):
    x = np.linspace(0, nut + 1)
    print(x[-1])
    y = np.linspace(0, 100)
    plt.plot(x, y, linewidth=0)
    ax = plt.gca()

    # Turn off tick labels
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    schicht_start = y[-1] / 2
    height = 10
    schicht_step = schicht_start
    for i in range(schicht + 1):
        p1 = [1, schicht_step]
        p2 = [2, schicht_step]
        newline(p1, p2)
        if i != schicht:
            rect = plt.Rectangle((-10, schicht_step), x[-1] * 2, height, color='#C0C0C0', alpha=1)
            plt.gca().add_patch(rect)
        schicht_step += height
    schicht_step = schicht_start

    colors = {0: ["#FFFF00", " a"], 1: ["#FF00FF", "-c"], 2: ["#99CC00", " b"]}
    color = 0
    width = 1
    height = height
    rect_num = {}

    gap = width / 4
    for steps in range(0, nut + 1, width):  # 0, 1, 2, 3, ... , nut+1
        x_annotation = (steps - width / 2) + gap / 2
        y_annotation = (schicht_step - height)
        rect_num[str(steps)] = mpatch.Rectangle((x_annotation, y_annotation),
                                                width - gap, height, color="#C0C0C0")

    wick_step = 0
    for i in range(schicht):
        for steps in range(0, nut, width):
            x_start = steps + gap / 2
            left, bottom, width_r, height_r = (x_start, schicht_step, width - gap, height)
            rect = plt.Rectangle((left, bottom), width_r, height_r, color=colors[color][0], alpha=1)
            add_annotation(colors[color][1], rect, axes=ax)
            plt.gca().add_patch(rect)
            wick_step += 1
            if wick_step == intv:
                color += 1
                wick_step = 0
                if color == 3:
                    color = 0
                    colors = reverse_dict(colors)
        wick_step += y_y0
        color = 0
        schicht_step += height

    for r in rect_num:
        add_annotation(r, rect_num[r], axes=ax)


""" Inputs """

N = 12
schicht = 1
m = 3
y = 10
y0 = 12

y_y0 = y0 - y
wicklung_interval = (N / m) / (N / y0)
plot_wicklungsplan(N, schicht, intv=wicklung_interval, y_y0=y_y0)

plt.show()
