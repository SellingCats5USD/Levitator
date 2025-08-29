import numpy as np

# Function to calculate phases for elements in the 6x7 array
# Passes to hostside which transmits serially over USB to a Teensy 4.1

# midpoint is at (3.5, 3)
# 10 mm diameter, 11mm pitch?
# how could I vectorize, or even OOP this?
# global and metric coordinate system or egocentric?
m = 6
n = 7
class Serial():
class Emitter():
    phase 
    position

class focus():
    position

def array(m, n, pitch):
    p = np.zeros((m*n, 3))
    idx = 0
    for i in range(m):
        for j in range(n):
            x = j * pitch
            y = i * pitch
            p[idx] = [x, y, 0]
            idx += 1
    return p

p = array(6, 7, 11)

for row_idx in range(m):
    start = row_idx * n
    end = start + n
    row = p[start:end]
    print(" ".join(f"({int(x):2d}, {int(y):2d}, {int(z):1d})" for x, y, z in row))

        
def distance(p):
    r = []
    for pos in p:
        r = np.sqrt((pos[0]**2) + pos[1]**2 + pos[2]**2)
    return r

print(djbvkhbvkebf)