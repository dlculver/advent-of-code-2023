import re
from typing import List

def get_full_numb(index: int, row: List[int]) -> int:

    n = len(row)

    if row[index].isdigit():
        left, right = index - 1, index + 1

        while row[left].isdigit() and left >= 0:
            left -= 1
        while right < n and row[right].isdigit():
            right += 1

        return int("".join(row[left + 1:right])), left + 1, right - 1
    
    # if row[index] is not an integer, just return 0. 
    # This should be okay since we are only looking for the sum of integers. 
    return 0




def sum_parts(grid: List[List[int]]) -> int:

    
    m, n = len(grid), len(grid[0])

    def is_valid(row: int, col: int) -> bool:
        return 0 <= row < m and 0 <= col < n

    adjacent_ints = []
    for row in range(m):
        for col in range(n):
            if grid[row][col] != "." and not grid[row][col].isdigit():
                # We've hit a symbol, so we need to look around.
                # We will look in all 8 directions, but we need different logic for each direction.
                # there should be a nice way to do this with graph methods.
                # for now, we will just do it manually.
                
                # start with left most
                # The logic here is start with the diagonal, see where the number ends. If it doesn't get to the middle, then check the right diagonal. 
                # in the event the left diagonal is ".", then check the middle. 
                if is_valid(row + 1, col - 1) and grid[row + 1][col - 1].isdigit():
                    number, start, end = get_full_numb(col - 1, grid[row + 1])
                    adjacent_ints.append(number)
                    if not end > col and grid[row + 1][col + 1].isdigit():
                        number, start, end = get_full_numb(col + 1, grid[row + 1])
                        adjacent_ints.append(number)
                elif is_valid(row + 1, col) and grid[row + 1][col].isdigit():
                    number, start, end = get_full_numb(col, grid[row + 1])
                    adjacent_ints.append(number)
                elif is_valid(row + 1, col + 1) and grid[row + 1][col + 1].isdigit():
                    number, start, end = get_full_numb(col + 1, grid[row + 1])
                    adjacent_ints.append(number)
                if is_valid(row - 1, col - 1) and grid[row - 1][col - 1].isdigit():
                    number, start, end = get_full_numb(col - 1, grid[row - 1])
                    adjacent_ints.append(number)
                    if not end > col and grid[row - 1][col + 1].isdigit():
                        number, start, end = get_full_numb(col + 1, grid[row - 1])
                        adjacent_ints.append(number)
                elif is_valid(row - 1, col) and grid[row - 1][col].isdigit():
                    number, start, end = get_full_numb(col, grid[row - 1])
                    adjacent_ints.append(number)
                elif is_valid(row - 1, col + 1) and grid[row - 1][col + 1].isdigit():
                    number, start, end = get_full_numb(col + 1, grid[row - 1])
                    adjacent_ints.append(number)
                # now check sides
                if is_valid(row, col - 1) and grid[row][col - 1].isdigit():
                    number, start, end = get_full_numb(col - 1, grid[row])
                    adjacent_ints.append(number)
                if is_valid(row, col + 1) and grid[row][col + 1].isdigit():
                    number, start, end = get_full_numb(col + 1, grid[row])
                    adjacent_ints.append(number)

    
    return sum(adjacent_ints)


def main():

    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [[c for c in line.strip()] for line in lines]

    print(sum_parts(grid))


if __name__ == "__main__":
    main()
