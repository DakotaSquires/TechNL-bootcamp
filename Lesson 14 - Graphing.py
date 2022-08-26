import matplotlib.pyplot as plt
from matplotlib import style

style.use("Solarize_Light2")
print(style.available)

# Create a function f1(x) = x2
def f1(x):
    return x ** 2


# Create a function f2(x) = x3
def f2(x):
    return x ** 3


# Create a function f3(x) = x/2
def f3(x):
    return x / 2


# Create a piecewise function using f1 where x < 0, and f3 where x >= 0
def f4(x):
    if x < 0:
        return f1(x)
    else:
        return f3(x)


fig, axs = plt.subplots(2, 2)


# range
xs = []
for i in range(-10, 11):
    xs.append(i)

# plotting
f1_ys = []
for x in xs:
    f1_ys.append(f1(x))
axs[0, 0].plot(xs, f1_ys, 'tab:green')
axs[0, 0].set_title("Axis [0, 0]")

f2_ys = []
for x in xs:
    f2_ys.append(f2(x))
axs[0, 1].plot(xs, f2_ys)
axs[0, 1].set_title("Axis [0, 1]")


f3_ys = []
for x in xs:
    f3_ys.append(f3(x))
axs[1, 0].plot(xs, f3_ys)
axs[1, 0].set_title("Axis [1, 0]")

f4_ys = []
for x in xs:
   f4_ys.append(f4(x))
axs[1, 1].plot(xs, f4_ys, 'tab:green')
axs[1, 1].set_title("Axis [1, 1]")

# Labels
for ax in axs.flat:
    ax.set(xlabel='Age (in years)', ylabel='Yearly Salary (in USD)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

# show
plt.show()

