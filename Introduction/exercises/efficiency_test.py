import numbers
import time
import random


# implementation 1
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result


# implementation 2
def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)


def run_time(function):
    n = 10**7
    print("n:", n)
    random.seed(10000)
    numbers = [random.randint(1, 10**7) for _ in range(n)]

    start_time = time.time()
    result = function(numbers)
    end_time = time.time()

    print("result:", result)
    print("time:", round(end_time - start_time, 2), "s")
    return result



print("result of implementation 1:", run_time(count_even))
print('---------------------------------------------------')
print("result of implementation 2:", run_time(count_even_2))


# print("result of implementation 2", run_time(count_even_2))