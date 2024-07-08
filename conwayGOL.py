import numpy as np
import cellpylib as cpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cellular_automaton = cpl.init_random2d(rows=100, cols=100)

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=250, neighbourhood='Moore',
                                  apply_rule=cpl.game_of_life_rule, memoize='recursive')

cpl.plot2d(cellular_automaton)

fig, ax = plt.subplots()
ax.set_xlim((0, 100))
ax.set_ylim((0, 100))

img = ax.imshow(cellular_automaton[0], interpolation='nearest', cmap='Greys')

def init():
    img.set_data(cellular_automaton[0])
    return (img,)

def animate(i):
    img.set_data(cellular_automaton[i])
    return (img,)

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=250, interval=30,
                              blit=True, repeat=False)

plt.show()