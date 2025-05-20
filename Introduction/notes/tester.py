import random
import time
from algorithms import *
from efficiency_measure import efficiency_measure

n = 1000
print("n: ", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for i in range(n)]

start_time = time.time()
result = max_diff(numbers)
end_time = time.time()

result1 = efficiency_measure(max_diff, [numbers, 1])
result2 = efficiency_measure(max_diff, [numbers, 2])
result3 = efficiency_measure(max_diff, [numbers, 3])

for n, i in enumerate([result1, result2, result3]):
    print(f"Result: {n+1}: {i[0]}, Time: {i[1]}")



