import matplotlib.pyplot as plt
from math import sin

def square_wave(x):
    return (
        sin(x)
        + 1 / 3 * sin(3 * x)
        + 1 / 5 * sin(5 * x)
        + 1 / 7 * sin(7 * x)
        + 1 / 9 * sin(9 * x)
    )


# Lower resolution
xs = [n / 5 for n in range(51)]
ys = [square_wave(x) for x in xs]
plt.plot(xs, ys, label="51 points")

# Higher resolution
xs = [n / 100 for n in range(1001)]
ys = [square_wave(x) for x in xs]
plt.plot(xs, ys, label="1001 points")

# plot labels
plt.title("Resolution example")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()
