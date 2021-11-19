import matplotlib.pyplot as plt
import matplotlib.animation as animation

# def read():
#     with open("C:/Users/5woodl59/OneDrive - Solent University/Documents/python imports") as temps:
#         csvread = csv.reader(temps)
#         headings = next(csv_reader)
#         data = {'week1': [], 'week2': []}
#
#         for values in csv_read:
#             data['week1'].append(values[0])
#             data['week2'].append(values[1])
#
#         return data
#
# def run():
#     data = read()
#     fig, axs = plt.subplots(2, 1, sharex="col")
#     days = range(1, 8)
#     axs[0].plot(days, data['week1'])
#     axs[1].plot(days, data['week2'])
#     plt.tight_layout()
#     plt.show()
#
# run()

fig, ax = pkt.subplots()

def animate(frame):
    print(frame)

def run():
    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)