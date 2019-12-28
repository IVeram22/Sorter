import allure

# O(n^2)
@allure.step("Bubble Sort.")
def bubble_sort(unsorted_list: list):
    counter = 0
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list)):
            if unsorted_list[i] < unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
            counter += 1
        counter += 1
    return counter
