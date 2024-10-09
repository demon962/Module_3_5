def calculate_structure_sum(*args):
    sum_numbers = 0
    total_length = 0

    def helper(data):
        nonlocal sum_numbers, total_length

        for element in data:
            if isinstance(element, (int, float)):
                sum_numbers += element
            elif isinstance(element, str):
                total_length += len(element)
            elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
                helper(element)
            elif isinstance(element, dict):
                for key, value in element.items():
                    if isinstance(key, (int, float)):
                        sum_numbers += key
                    elif isinstance(key, str):
                        total_length += len(key)
                    if isinstance(value, (int, float)):
                        sum_numbers += value
                    elif isinstance(value, str):
                        total_length += len(value)
                    elif isinstance(value, (list, tuple, set)):
                        helper(value)

    for arg in args:
        helper(arg)

    return sum_numbers, total_length

result = calculate_structure_sum(
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
)

print("Сумма всех чисел:", result[0])
print("Сумма длин всех строк:", result[1])