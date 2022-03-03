import numpy as np

np.random.uniform(0, 1)

for i in range(0, 5):
    a = input("Тяните Жребий (Enter)")
    x = np.random.uniform(0, 10)
    if x < 2:
        print('Вы проиграли')
    else:
        print('Вы выиграли')



