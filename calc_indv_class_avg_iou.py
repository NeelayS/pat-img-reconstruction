import numpy as np

d = np.array([0, 0, 0, 0])

with open("logs.txt", "r") as f:
    lines = f.readlines()
    for i in range(2, len(lines)-1):
        a = lines[i].split("[")[1]
        b = a.split("]")[0]
        c = b.split(",")
        c = list(map(float, b.split(",")))[:4]
        print(type(c), len(c), c)
        d = np.vstack((d, np.array(c)))

print(type(d), len(d), d[42])
print(d.shape)

d = d[1:, :]
print(d.shape)

m = np.mean(d, axis=0)
print(m)
print(np.mean(m))

# The IoUs for the individual classes (tissue categories) were 0.9942, 0.7792, 0.9351, and 0.8556 respectively.