def bubble_sort(numbers):
    list_len = len(numbers) - 1

    for i in range(list_len):
        for ind in range(list_len - i):
            if numbers[ind] > numbers[ind + 1]:
                swap = numbers[ind]
                numbers[ind] = numbers[ind + 1]
                numbers[ind + 1] = swap

    return numbers


def insertion_sort(numbers):
    list_len = len(numbers)

    for i in range(1, list_len):
        numb1 = numbers[i]
        ind = i - 1
        while ind >= 0 and numb1 < numbers[ind]:
            numbers[ind + 1] = numbers[ind]
            ind -= 1

        numbers[ind + 1] = numb1

    return numbers


def main():

    while True:
        try:
            input_list = input("Enter a list of numbers separated by commas: ")
            original_numbers = [float(x) for x in input_list.split(',')]

            print("Choose which algorithm you want to use:")
            print("1. Bubble Sort\n2. Insertion Sort")
            choice = int(input("Input the number of the algorithm: "))

            if choice == 1:
                numbers = original_numbers.copy()
                bubble_sort(numbers)

                print(f'\nYour list: {original_numbers}')
                print(f"Sorted with bubble sort: {numbers}")
            elif choice == 2:
                numbers = original_numbers.copy()
                insertion_sort(numbers)

                print(f'\nYour list: {original_numbers}')
                print(f"Sorted with insertion sort: {numbers}")
            else:
                print("This number doesn't correspond to an algorithm.")
                continue

            break

        except ValueError:
            print("Please enter a valid list of numbers. Example: 6.7, 3, -9, 67")


if __name__ == "__main__":
    main()




















