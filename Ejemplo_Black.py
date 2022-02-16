import pandas as pd


def foo():
    print("foo")


a = [1, 2, 3, 4, 5, 7]

b = {
    "first": 100,
    "second": 50,
    "third": 23,
    "fourth": 99,
    "fufth": 77,
    "sixth": 66,
    "seventh": 54,
    "eighth": 88,
}


def my_cool_function(
    input_size,
    output_size,
    num_classes=2,
    num_features=5,
    print_output=True,
    include_log=False,
):
    if print_output:
        print(input_size, output_size, num_classes, num_features)
