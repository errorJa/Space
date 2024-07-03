import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

fig, axes = plt.subplots(2)
fig.set_facecolor('#D3D3D3')
camera = Camera(fig)
axes[0].grid()
axes[1].grid()


t = np.linspace(0, 4 * np.pi, 1000, endpoint=False)

for i in t:
    axes[0].plot(t, np.sin(t + i), color='r')
    axes[1].plot(t, np.sin(t - i), color='b')
    camera.snap()

a = camera.animate()
plt.show()
a.save('waves2.mp4', fps=60)
