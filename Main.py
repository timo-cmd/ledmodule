from oxocard import *

for y in range(8):
    for x in range(8):  
        if (x + y) % 2 == 0 :
            dot(x, y, BLUE)
        else:
            dot(x, y, WHITE)  
