def length_string(string):
    """Приймає рядок і повертає його довжину."""
    return len(string)

def sum_strings(string1, string2):
    """Приймає два рядки і повертає об'єднаний рядок."""
    return string1 + string2

def square_number(number):
    """Приймає число і повертає його квадрат."""
    return number ** 2

def sum_numbers(a, b):
    """Приймає два числа і повертає їхню суму."""
    return a + b

def division_remainder(dividend, divisor):
    """Приймає 2 числа типу int, виконує операцію ділення та повертає цілу частину і залишок."""
    integer = dividend // divisor
    remainder = dividend % divisor
    return integer, remainder

def average_list(numbers):
    """Обчислення середнього значення списку чисел."""
    if not numbers:
        return None  # Повертає None, якщо список порожній, бо на нуль ділити не можна
    return sum(numbers) / len(numbers)

def common_elements(list1, list2):
    """Приймає два списки і повертає список, який містить спільні елементи обох списків."""
    return list(set(list1) & set(list2))

def print_keys(dictionary):
    """Приймає словник і виводить всі ключі цього словника."""
    for key in dictionary.keys():
        print(key)

def merge_dicts(dict1, dict2):
    """"Приймає два словники і повертає новий словник, який є об'єднанням обох словників."""
    merged_dict = {}
    merged_dict.update(dict1)
    merged_dict.update(dict2)
    return merged_dict

def union_of_sets(set1, set2):
    """"Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання."""
    return set1.union(set2)

def is_subset(set1, set2):
    """"Перевіряє, чи є одна множина підмножиною іншої."""
    return set1.issubset(set2)

def check_even_odd(number):
    """"Приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне."""
    if number % 2 == 0:
        print("Парне")
    else:
        print("Непарне")

def filter_numbers(numbers):
    """Приймає список чисел і повертає новий список, що містить тільки парні числа."""
    return [num for num in numbers if num % 2 == 0]
