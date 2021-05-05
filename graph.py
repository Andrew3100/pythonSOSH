import matplotlib.pyplot as plt
import random
import numpy
import linalg
import numpy as np

r1 = random.randint(5, 10)
r2 = random.randint(5, 10)
r3 = random.randint(5, 10)
r4 = random.randint(5, 10)
array = [1, r1, r3, 1]
array1 = [10, r2, r4, 10]
test = '-4 -1 2; 10 4 -1; 8 3 1'
matr = np.matrix(test)


print(np.linalg.det(matr))

plt.plot(array, array1)

plt.show()

print('Вычислено')
