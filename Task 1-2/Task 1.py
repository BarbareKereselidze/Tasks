""" Binary search recursive algorithm
    Binary search-ის time complexity არის O(log n), რადგან ელემენტების რაოდენობა n-ია,
    და რეკურსიის ყოველი გამოყენებისას საძებნი ელემენტების რაოდენობა ნახევარზე იყოფა.
    რეკურსიული binary search-ის დროს O(log n)-ია, რადგან ყველაზე ცუდ შემხვევაში O(log n)-ჯერ მოხდება რეკურსია,
    შესაბამისად ყველა რეკურსია ინახება memory-ში.
    """


# def binary_search(numbers, dzebnili, low=0, high=None):
#
#     if high is None:
#         high = len(numbers) - 1
#
#     mid = (low + high) // 2
#     # print(low, mid, high)
#
#     if high >= low:
#         if dzebnili == numbers[mid]:
#             return f'dzebnili is the {mid}th element'
#         elif dzebnili > numbers[mid]:
#             return binary_search(numbers, dzebnili, mid + 1, high)
#         else:
#             return binary_search(numbers, dzebnili, low, mid - 1)
#     else:
#         return 'dzebnili is not in the array'


# numbs = [7.8, 8.9, 10, 17, 58, 67, 98, 102]
# target = 7.8

# print(binary_search(numbs, target))


""" Linear search algorithm 
    Linear search-ის time complexity არის O(n), რადგან ყევლაზე ცუდ შემთხვევაში უწევს, 
    მთლიანი n ელემენტის რაოდენობიანი ლისტის გავლა რათა იპოვოს ელემენტი.
    Space complexity არის O(1) იმიტომ რომ ნებისმიერ შემთხვევაში მხოლოდ ორ ელემენტს ვადარებთ ერთმანეთს,
    იმ ელემენტს რომელსაც ვეძებთ და ლისტის ერთ-ერთ ელემენტს.
    """


# def linear_search(numbers, dzebnili):
#     list_len = len(numbers)
#
#     for ind in range(list_len):
#         if dzebnili == numbers[ind]:
#             return f'dzebnili is the {ind}th element'
#     else:
#         return 'dzebnili daikarga'
#
#
# numbs = [7.8, 8.9, 10, 17, 58, 67, 98, 102]
# target = 102
#
# print(linear_search(numbs, target))



