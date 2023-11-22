from sorting_algorithms import output_result
from input_processing import get_list, get_algorithm, output_result
import click


@click.command()
def main():
    input_list = get_list()
    input_algorithm = get_algorithm()

    output_result(input_list, input_algorithm)


if __name__ == "__main__":
    main()

