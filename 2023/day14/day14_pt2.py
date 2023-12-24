# --- Day 14: Parabolic Reflector Dish Part 2---
# reminder: every user has a distinct input given to them by advent of code
"""
this is a bit of a brute force solution that actually does not yield a result we can use due to the recursion limit,
it only goes up to 248 cycles where we would need 1000000000

After 3 cycles it yields the same matrix given in the example, so I am going to carefully assume the logic is generally correct

Theoretically, if we were to reach 1000000000 cycles and yield a matrix,
the logic from part 1 could be applied on that matrix and we would get the correct result

Maybe I will come back to this later, now time for Christmas!
"""
from typing import List, Literal

example = True # change this flag to switch input files
input_file = ""
if example: input_file = "example_input.txt"
else: input_file = "main_input.txt"

with open(input_file, "r") as f:
    sample_input = list(map(str.strip, f.readlines()))

def tilt(
    dish: List[List[str]],
    orientation: Literal["north", "south", "west", "east"],
    iteration: int,
    cycle:int
):
    if cycle == 3: # change cycle
        return

    if orientation == "north" or orientation == "south":
        col_list = []
        for x in range(len(sample_input)):
            lst = []
            for line in dish: lst.append(line[x])
            col_list.append(lst)
        dish = col_list

    row_matrix = {x:[] for x in range(len(sample_input))}
    row_or_col = 0
    for idx, l in enumerate(dish):
        new_dish = "".join(l).split("#")
        for y_idx, y in enumerate(new_dish):
            o_count = y.count("O")
            list_length = 0 if orientation in ["north", "west"] else len(y)
            for lst in new_dish[:y_idx]: list_length += len(lst)+1 # number of lists before current list + the lengths of those lists
            if orientation == "north":
                for c in range(list_length, list_length + o_count):
                    row_matrix[c].append(row_or_col)
            if orientation == "south":
                for c in range(list_length-1, list_length - (o_count+1), -1):
                    row_matrix[c].append(row_or_col)
            if orientation == "west":
                for c in range(list_length, list_length + o_count):
                    row_matrix[row_or_col].append(c)
            if orientation == "east":
                for c in range(list_length-1, list_length - (o_count+1), -1):
                    row_matrix[row_or_col].append(c)

        row_or_col += 1 # goes to next column when north or south, goes to next row when west or east

    all_rows = []
    print(f"cycle {cycle+1}: orientation {orientation}")
    print("----------")
    for idx, row in enumerate(sample_input): # use sample_input as template
        row = list(row)
        for col_idx, char in enumerate(row):
            if char == "O": row[col_idx] = "."
            if col_idx in row_matrix[idx]:
                row[col_idx] = "O"
        all_rows.append(row)
        print(row)

    orientation_mapping = {
        "north":"west",
        "west": "south",
        "south": "east",
        "east": "north"
    }

    orientation = orientation_mapping[orientation]
    iteration += 1
    if iteration == 4:
        cycle += 1; iteration = 0
    tilt(all_rows, orientation, iteration, cycle)


tilt(sample_input, "north", 0, 0)
