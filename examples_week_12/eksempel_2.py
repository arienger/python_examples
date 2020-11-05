import matplotlib.pyplot as plt
from math import sin

xs = [n / 10 for n in range(101)]
ys = [sin(x) for x in xs]

plt.subplot(221)
plt.plot(xs, ys, "-.r")
plt.ylabel("y")

plt.subplot(222)
plt.plot(xs, [3 * y for y in ys], "--y")

plt.subplot(223)
plt.plot(xs, ys, "-.k")
plt.xlabel("x")

plt.subplot(224)
plt.plot(xs, [3 * y for y in ys], "--b")

plt.suptitle("Several plots")
plt.show()
