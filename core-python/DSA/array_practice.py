import array
import random

temps = array.array('i', [random.randint(-100, 0) for _ in range(24)])

max_temp = temps[0]
max_hour = 0
min_temp = temps[0]
min_hour = 0

for i in range(len(temps)):
    if temps[i] > max_temp:
        max_temp = temps[i]
        max_hour = i
    if temps[i] < min_temp:
        min_temp = temps[i]
        min_hour = i

avg_temp = sum(temps) / len(temps)

with open('../data/mars_temps.txt', 'w', encoding='utf-8') as f:
    f.write(f"Max temperature: {max_temp} at hour {max_hour}\n")
    f.write(f"Min temperature: {min_temp} at hour {min_hour}\n")
    f.write(f"Average temperature: {avg_temp:.2f}\n")

with open('../data/mars_temps.txt', 'r', encoding='utf-8') as f:
    print(f.read())
    j
