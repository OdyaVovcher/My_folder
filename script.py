#Считает среднее массива случайных чисел

import random

N = 10
s = 0
arr = [random.randint(1,10) for i in range(N)]

for i in arr:
	s += i

mean = s/len(arr)

print(f"Среднее: {mean}")