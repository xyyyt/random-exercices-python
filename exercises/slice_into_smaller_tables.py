from typing import List, Tuple
import pytest

def check_table_is_sliceable(table : List[List[int]], slice_nb : int) -> None:
    if len(table) < slice_nb:
        raise ValueError(f"row max must be at least equal to {slice_nb}"
                         " to slice table")
    elif len(table[0]) < slice_nb:
        raise ValueError(f"column max must be at least equal to {slice_nb}"
                         " to slice table")

def check_slice_nb(slice_nb : int) -> None:
    if slice_nb < 2:
        raise ValueError("'slice_nb' parameter cannot be less than 2 to slice table")

def check_table_has_same_size_for_all_columns(table : List[List[int]]) -> None:
    required_size : int = len(table[0])

    for array in table[1:]:
        if len(array) != required_size:
            raise ValueError("'table' parameter must have the same size for all columns")

def check_table_is_empty(table : List[List[int]]) -> None:
    if not table:
        raise ValueError("'table' parameter cannot be empty")

def check_table(table : List[List[int]], slice_nb : int) -> None:
    check_table_is_empty(table)
    check_table_has_same_size_for_all_columns(table)
    check_slice_nb(slice_nb)
    check_table_is_sliceable(table, slice_nb)

def slice_into_smaller_tables(table : List[List[int]], slice_nb : int = 2) \
    -> List[List[List[int]]]:
    check_table(table, slice_nb)

    row_max : int = len(table)
    column_max : int = len(table[0])
    new_tables : List[List[List[int]]] = []

    for row in range(0, row_max, slice_nb):
        row2 : int = row
        column : int = 0
        new_table : List[List[int]] = []

        while column < column_max:
            new_table.append(table[row2][column:column + slice_nb])
            row2 += 1

            if row2 % slice_nb == 0 or row2 >= row_max:
                if row2 % slice_nb == 0:
                    new_tables.append(new_table)
                    new_table = []

                row2 = row
                column += slice_nb

        if new_table:
            new_tables.append(new_table)

    return new_tables

@pytest.mark.parametrize("parameter", [
    ([], ), # check table isn't empty
    ([[1, 2],
      [3, 4, 5]], ), # check table has same size for all columns
    ([[1, 2],
      [3, 4]],
     1), # check slice number is equal or greater than 2
    ([[1, 2, 3, 4],
      [5, 6, 7, 8]],
     3), # check slice number is equal or greater than max row
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [10, 11, 12]],
     4)]) # check slice number is equal or greater than max columns
def test_slice_into_smaller_tables__raise_value_error(
        parameter : Tuple[List[List[int]], int]) -> None:
    with pytest.raises(ValueError):
        slice_into_smaller_tables(*parameter)

@pytest.mark.parametrize("parameter, expected", [
    (([[1, 2],
       [3, 4]],
      2),
     [
         [
             [1, 2],
             [3, 4]
         ]
     ]),
    (([[1, 2, 3],
       [4, 5, 6]],
      2),
     [
         [
             [1, 2],
             [4, 5]
         ],
         [
             [3],
             [6]
         ]
     ]),
    (([[1, 2, 3, 4],
       [5, 6, 7, 8]],
      2),
     [
         [
             [1, 2],
             [5, 6]
         ],
         [
             [3, 4],
             [7, 8]
         ]
     ]),
    (([[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]],
      3),
     [
         [
             [1, 2, 3],
             [6, 7, 8],
             [11, 12, 13]
         ],
         [
             [4, 5],
             [9, 10],
             [14, 15]
         ],
         [
             [16, 17, 18],
             [19, 20]
         ]
     ]),
    (([[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]],
      5),
     [
         [
             [1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ]
     ]),
    (([[1, 2, 3, 4, 5, 6, 7],
       [8, 9, 10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19, 20, 21],
       [22, 23, 24, 25, 26, 27, 28],
       [29, 30, 31, 32, 33, 34, 35],
       [36, 37, 38, 39, 40, 41, 42]],
      6),
     [
         [
             [1, 2, 3, 4, 5, 6],
             [8, 9, 10, 11, 12, 13],
             [15, 16, 17, 18, 19, 20],
             [22, 23, 24, 25, 26, 27],
             [29, 30, 31, 32, 33, 34],
             [36, 37, 38, 39, 40, 41]
         ],
         [
             [7],
             [14],
             [21],
             [28],
             [35],
             [42]
         ]
     ])])
def test_slice_into_smaller_tables(
        parameter : Tuple[List[List[int]], int],
        expected : List[List[List[int]]]) -> None:
    assert slice_into_smaller_tables(*parameter) == expected
