import numpy as np
import matplotlib.pyplot as plt
list_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numpy_array = np.array(list_array)

def function(input_array):

    y= x ** (1/3)
    return y

x = np.arange(0,100)
y = function(x)

plt.plot(x,y)
plt.show()