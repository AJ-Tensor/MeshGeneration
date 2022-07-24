import numpy as np
import math
import matplotlib.pyplot as plt
L = 1
h = 1
r = 0.3
c = [0.5, 0.5]

numberOfElementsx = 100
numberOfElementsy = 50

Nodes = []
#
# for x in np.linspace(0, L, numberOfElementsx):
#     if x < r:
#         y0 = math.sqrt(r**2-x**2)
#         for y in np.linspace(y0, h, numberOfElementsy):
#             Nodes.append([x, y])
#     else:
#         for y in np.linspace(0, h, numberOfElementsy):
#             Nodes.append([x, y])

for x in np.linspace(0, L, numberOfElementsx):
    if 0.5 - r <= x < 0.5 + r:
        y0 = 0.5 - math.sqrt(r*r-((x-0.5)*(x-0.5)))
        y1 = 0.5 + math.sqrt(r*r-((x-0.5)*(x-0.5)))
        for y in np.linspace(0, y0, numberOfElementsy):
            Nodes.append([x, y])
        for y in np.linspace(y1, h, numberOfElementsy):
            Nodes.append([x, y])
    else:
        for y in np.linspace(0, h, numberOfElementsy):
            Nodes.append([x, y])

Nodes = np.array(Nodes)

plt.plot(Nodes[:, 0], Nodes[:, 1],'+')
plt.show()
print(Nodes)


