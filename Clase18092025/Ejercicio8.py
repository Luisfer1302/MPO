import random
import statistics 

tiradas = list()
repeticiones = list() [6]

for i in range(10):
    tirada = random.randint(1, 6)
    tiradas.append(tirada)
    repeticiones[tirada-1] += 1
reps = -1
moda = 0
for i in range(6):
    if repeticiones[i] > reps:
        moda = i
        reps = repeticiones[i]

print(f"Las tiradas han sido{tiradas}")
print(f"El primer más repetido es {moda+1}")