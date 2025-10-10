main_list = [5, 2, 9, 8, 1, 6, 3, 7, 4, 10,
             "яблуко", "груша", "слива", "банан", "апельсин",
             "вишня", "ананас", "черешня", "диня", "ківі"]
numbers = [x for x in main_list if type(x) == int]
strings = [x for x in main_list if type(x) == str]
numbers.sort()
strings.sort()
sorted_list = numbers + strings
even_numbers = [x for x in numbers if x % 2 == 0]
upper_strings = [x.upper() for x in strings]
print("Головний відсортований список:", sorted_list)
print("Список парних чисел:", even_numbers)
print("Список рядків КАПСОМ:", upper_strings)
