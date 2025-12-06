#N1
numbers = [15, 8, 22, 3, 45, 1, 30]
even_numbers =list(filter(lambda a:a > 10,numbers))
print(even_numbers)
#N2
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
even_words =list(filter(lambda b: len(b) < 6,words))
print(even_words)
#N3
employees = [
    {'name': 'Іван', 'role': 'Manager', 'salary': 50000},
    {'name': 'Анна', 'role': 'Developer', 'salary': 60000},
    {'name': 'Марія', 'role': 'Manager', 'salary': 70000},
    {'name': 'Олег', 'role': 'Intern', 'salary': 20000}
]
even_employees =list(filter(lambda emp:emp["role"] == "Manager",employees))
print(even_employees)
