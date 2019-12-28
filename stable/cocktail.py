import allure

# O(n^2)
@allure.step("Cocktail Sort.")
def cocktail_sort(unsorted_list: list):
    counter = 0
    left = 0
    right = len(unsorted_list) - 1
    while left <= right:
        for i in range(left, right):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
            counter += 1
        right -= 1

        for j in range(right, left, -1):
            if unsorted_list[j - 1] > unsorted_list[j]:
                unsorted_list[j - 1], unsorted_list[j] = unsorted_list[j], unsorted_list[j - 1]
            counter += 1
        left += 1

        counter += 1
    return counter
