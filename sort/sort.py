from randomer.list import get_random_list
import allure


@allure.step("Check Is list sorted?")
def is_list_sorted(sorted_list: list):
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                return False

    return True


@allure.step("Is list sorted?")
def hard_assert_true(result: bool):
    print("Is list sorted? - {}.".format(result))
    assert result


def sort(**kwargs):
    def inner(fun):
        def wrapper():
            length = kwargs["length"]
            min_value = kwargs["min_value"]
            max_value = kwargs["max_value"]

            my_list = get_random_list(length, min_value, max_value)
            print("Random list: {}".format(my_list))
            counter = fun(my_list)
            print("Sort list:   {}".format(my_list))
            print("Counter: {}".format(counter))
            result = is_list_sorted(my_list)
            hard_assert_true(result)
            return result

        return wrapper

    return inner
