from random import randint
import allure


@allure.step("Create Random List.")
def get_random_list(length: int = 10, min_value: int = 0, max_value: int = 100):
    new_list = []
    for i in range(length):
        new_list.append(randint(min_value, max_value))
    return new_list
