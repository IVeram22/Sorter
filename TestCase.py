import pytest
import allure
from sort.sort import sort
from stable.bubble import bubble_sort
from stable.cocktail import cocktail_sort
from stable.insertion import insertion_sort


@sort(length=10, min_value=-100, max_value=100)
def test_bubble_sort(unsorted_list: list):
    return bubble_sort(unsorted_list)


@sort(length=10, min_value=-100, max_value=100)
def test_cocktail_sort(unsorted_list: list):
    return cocktail_sort(unsorted_list)


@sort(length=10, min_value=-100, max_value=100)
def test_insertion_sort(unsorted_list: list):
    return insertion_sort(unsorted_list)
