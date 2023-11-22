import functools


def output_result(sorting_function):
    """ Decorator function that outputs a result of a sorting function
        is used to avoid if else block in the main function and provides the freedom to add more sorting algorithms. """
    @functools.wraps(sorting_function)
    def wrapper(numbers):
        result = sorting_function(numbers)
        return result

    return wrapper


@output_result
def bubble_sort(numbers):
    list_len = len(numbers) - 1

    for i in range(list_len):
        for ind in range(list_len - i):
            if numbers[ind] > numbers[ind + 1]:
                swap = numbers[ind]
                numbers[ind] = numbers[ind + 1]
                numbers[ind + 1] = swap

    return numbers


@output_result
def insertion_sort(numbers):
    len_of_list = len(numbers)

    for i in range(1, len_of_list):
        numb1 = numbers[i]
        ind = i - 1
        while ind >= 0 and numb1 < numbers[ind]:
            numbers[ind + 1] = numbers[ind]
            ind -= 1

        numbers[ind + 1] = numb1

    return numbers


@output_result
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    # choosing the pivot (last element)
    pivot = numbers[-1]

    smaller_than = []
    mid = []
    larger_than = []

    for x in numbers:
        if x < pivot:
            smaller_than.append(x)
        elif x > pivot:
            larger_than.append(x)
        else:
            mid.append(pivot)

    return quick_sort(smaller_than) + mid + quick_sort(larger_than)


# Corresponding algorithm numbers to algorithms
sorting_algorithms = {
    1: bubble_sort,
    2: insertion_sort,
    3: quick_sort,
}