import allure

# O(n^2)
@allure.step("Insertion Sort.")
def insertion_sort(unsorted_list: list):
    counter = 0
    for i in range(len(unsorted_list)):
        element = unsorted_list[i]
        j = i
        while j > 0 and unsorted_list[j - 1] > element:
            unsorted_list[j] = unsorted_list[j - 1]
            j -= 1
            counter += 1
        unsorted_list[j] = element
        counter += 1

    return counter
