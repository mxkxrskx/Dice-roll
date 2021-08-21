import matplotlib.pyplot as plt
from die import Die

edge_1 = 6
edge_2 = 6
die_1 = Die(edge_1)
die_2 = Die(edge_2)

while True:
#Modelling situation
    times = 50000
    results = [die_1.roll() + die_2.roll() for i in range(times)]

#Analysis results
    max_results = die_1.num_sides + die_2.num_sides
    frequencies = [results.count(value) for value in range(1, max_results+1)]

    x = list(range(1, max_results+1))
    width = 0.1
#Visualization results
    fig, ax = plt.subplots()
    viz = ax.bar(x, frequencies, width)

#Some text
    ax.set_title(f'Results of rolling D{edge_1} and D{edge_2} {times} times')
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Result')

    ax.bar_label(viz)
    plt.show()

    ans = input('Make another visualization? (y/n) ')
    if ans.lower() == 'n':
        break
