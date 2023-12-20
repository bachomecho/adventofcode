# --- Day 14: Parabolic Reflector Dish ---

example = False # change this flag to switch input files
input_file = ""
if example: input_file = "example_input.txt"
else: input_file = "main_input.txt"

with open(input_file, "r") as f:
    input = list(map(str.strip, f.readlines()))

col_list = []
for x in range(len(input[0])):
    lst = []
    for line in input: lst.append(line[x])
    col_list.append(lst)

result = 0
for l in col_list:
    pressure = 0
    pressure_score = len(l)
    new_col = "".join(l).split("#")
    for y in new_col:
        other_elems = 0
        if not y:
            pressure_score -= 1
            continue
        for idx, char in enumerate(y):
            if char == "O":
                pressure += pressure_score
                pressure_score -= 1
            else: other_elems += 1
        pressure_score -= other_elems + 1
    result += pressure
print(result)
