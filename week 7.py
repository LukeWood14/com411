import matplotlib.pyplot as plt
import random
import csv
# x = [0, 5, 10]
# y = [0, 50 ,100]
# plt.plot(x, y)
# plt.show()

# def display(x, y):
#     plt.plot(x, y)
#     plt.show()
#
# def run():
#     x_values = [1, 2, 3, 4, 5]
#     y_values = [1, 4, 9, 16, 25]
#     display(x_values, y_values)
#
# run()

# def small():
#     x = [5, 5, 6, 6, 5]
#     y = [5, 6, 6, 5, 5]
#     plt.plot(x, y, 'ro:')
#
# def medium():
#     x = [4, 4, 7, 7, 4]
#     y = [4, 7, 7, 4, 4]
#     plt.plot(x, y, 'gs--')
#
# def large():
#     x = [3, 3, 8, 8, 3]
#     y = [3, 8, 8, 3, 3]
#     plt.plot(x, y, 'bp-')
#
# def run():
#     small()
#     medium()
#     large()
#     plt.show()
#
# run()

# def coord():
#     x = int(input("enter an x coordinate: "))
#     y = int(input("enter a y coordinate: "))
#     coordinate=(x,y)
#     return coordinate
#
# def path():
#     print("Retrieving path...")
#     coords = []
#     xvals = []
#     yvals = []
#     x = 0
#     while x < 4:
#         co = coord()
#         x_val = co[0]
#         y_val = co[1]
#         xy = (x_val, y_val)
#         xvals.append(x_val)
#         yvals.append(y_val)
#         coords.append(xy)
#         x = x+1
#     print(coords)
#     return [xvals, yvals]
#
# def run():
#     values = path()
#     plt.plot(values[0], values[1], 'ro--')
#     plt.show()
#
# run()

# def data():
#     paths = {}
#     linestyle = input("style of line? :/--/- ")
#     linecol = input("colour of lines? r/g/b ")
#     marker = input("marker type? o/s/^ ")
#     paths["style"] = linestyle
#     paths["col"] = linecol
#     paths["marker"] = marker
#     return paths
#
# def generate():
#     lineNo = int(input("line number: "))
#     while lineNo > 0:
#         print("next line")
#         x = random.sample(range(1, 10), 5)
#         y = random.sample(range(1, 10), 5)
#         values = data()
#         design = (f"{values['style']}{values['col']}{values['marker']}")
#         plt.plot(x, y, design)
#         lineNo = lineNo - 1
#     plt.show()
#
# def run():
#     generate()
#
# run()

def read_data(data):
    temps = []
    with open(data) as file:
        for line in file:
            temps.append(float(line.strip()))
    print(temps)
    return temps

def run():
    data = "C:/Users/5woodl59/OneDrive - Solent University/Documents/python imports"
    read_data(data)

run()
