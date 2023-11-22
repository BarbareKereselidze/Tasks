import click
from sorting_algorithms import sorting_algorithms


def get_list():
    try:
        list_of_numbers = click.prompt("Enter a list of numbers separated by commas")
        return [float(x) for x in list_of_numbers.split(',')]
    except (ValueError, TypeError):
        click.echo("Please enter a valid list of numbers.")
        raise click.Abort()


def get_algorithm():
    click.echo("\nChoose which algorithm you want to use")

    for key, algorithm in sorting_algorithms.items():
        click.echo(f"{key}. {algorithm.__name__.replace('_', ' ')}")

    sorting_algorithm = click.prompt("Input the number of the algorithm\nYour Choice", type=int)

    if sorting_algorithm not in sorting_algorithms:
        click.echo("This number doesn't correspond to an algorithm.")
        raise click.Abort()

    return sorting_algorithms[sorting_algorithm]


def output_result(original_numbers, selected_algorithm):
    result = selected_algorithm(original_numbers)
    algorithm_name = selected_algorithm.__name__.replace("_", " ")

    click.echo(f'\nYour list: {original_numbers}')
    click.echo(f"Sorted with {algorithm_name}")
    click.echo(f"Sorted numbers: {result}")
