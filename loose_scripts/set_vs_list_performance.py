"""
Function which will check if given value is in the provided set or list.
Check which method is faster.

"""
import time


def function_performance(func, *arg, how_many_times=1):
    sum = 0
    for i in range(how_many_times):
        start = time.perf_counter_ns()
        func(*arg)
        end = time.perf_counter_ns()
        sum = sum + (end - start)
    return sum


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]


def value_in_container_checker(value, container):
    if value in container:
        return "The given value is in the provided container."

    elif value not in container:
        return "The given value is NOT in the provided container."


print(function_performance(value_in_container_checker,
      1000, setContainer, how_many_times=10))
print(function_performance(value_in_container_checker,
      1000, listContainer, how_many_times=10))
