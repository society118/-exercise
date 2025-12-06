import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція '{func.__name__}' виконана за {execution_time:.4f} секунд.")
        return result
    return wrapper

@timer
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

@timer
def power_of_numbers(numbers):
    return [num ** 2 for num in numbers]

sum_result = calculate_sum(10000000)
print(f"Результат суми: {sum_result}\n")

numbers_list = list(range(1000000))
squared_numbers = power_of_numbers(numbers_list)
print("Довжина списку з квадратами чисел:", len(squared_numbers))