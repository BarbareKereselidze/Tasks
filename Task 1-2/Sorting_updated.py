import functools
import click


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


# Using click dictionary for a command line interface
@click.command()
@click.option("--list_of_numbers", prompt="Enter a list of numbers separated by commas",
              help="Example: 6.7, 3, -9, 67")
# @click.option("--sorting_algorithm", prompt="Choose which algorithm you want to use\n"
#                                             "1. Bubble Sort\n2. Insertion Sort\n3. Quick Sort",
#               type=int, help="Input the number of the algorithm")
def main(list_of_numbers):

    try:
        # turning string input into a list of numbers
        original_numbers = [float(x) for x in list_of_numbers.split(',')]
    except (ValueError, UnboundLocalError):
        # Handling wrong input of lists
        click.echo("Please enter a valid list of numbers.")
        raise click.Abort()

    click.echo("\nChoose which algorithm you want to use")

    sorting_algorithm = click.prompt("Input the number of the algorithm\n"
                                     "1. Bubble Sort\n2. Insertion Sort\n3. Quick Sort\nYour Choice:", type=int)

    selected_algorithm = sorting_algorithms.get(sorting_algorithm)
    if selected_algorithm is None:
        # Handling wrong input of algorithm
        click.echo("This number doesn't correspond to an algorithm.")
        raise click.Abort()

    # sorting list and displaying the results
    result = selected_algorithm(original_numbers)
    algorithm_name = selected_algorithm.__name__
    algorithm_name = algorithm_name.replace("_", " ")

    click.echo(f'\nYour list: {original_numbers}')
    click.echo(f"Sorted with {algorithm_name}")
    click.echo(f"Sorted numbers: {result}")


if __name__ == "__main__":
    main()
