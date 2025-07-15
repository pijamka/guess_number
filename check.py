def find_max_even_number(number: list):
    """
    Ищет максимальное чётное значение в списке положительных целых значений, 
    переданном в параметр функции.
    """
    CurrentMax = 0

    for digit in number:
        if digit % 2 == 0:
            CurrentMax = max(digit, CurrentMax)
    return CurrentMax


max_even = find_max_even_number([1, 2, 3, 4, 5])
# Попробуйте передать в find_max_even_number() другие списки:
# [10, 8, 6, 4, 2]
# [2, 12, 85, 0, 6]
print(f"Максимальное чётное число: {max_even}")
