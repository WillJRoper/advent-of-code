"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola
lift will take you up to the water source, but this is as far as he can bring
you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
 right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation
of the engine. There are lots of numbers and symbols you don't really
understand, but apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum. (Periods (.) do not
count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all
of the part numbers in the engine schematic?

--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the
engine springs to life, you jump in the closest gondola, finally ready to
ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong?
Fortunately, the gondola has a phone labeled "help", so you pick it up and the
engineer answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and waving with
the other. You're going so slowly that you haven't even left the station. You
exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is
wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its
gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up
so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it
has part numbers 467 and 35, so its gear ratio is 16345. The second gear is
in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a
gear because it is only adjacent to one part number.) Adding up all of the gear
ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
import sys
import re
import numpy as np


def contains_symbols(line, ind, ntest):
    """
    Test if string contains nonnumeric characters that are not '.'.

    Args:
        line (string)
            The line to test.
        ind (int)
            The position of the string to test.
        ntest (int)
            The number of characters to test.

    Returns:
        bool
    """
    low = ind - 1 if ind > 0 else 0
    up = ind + ntest if ind + ntest < len(line) else len(line)
    chars = line[low:up]
    symbols = "".join([s for s in chars.replace(".", "") if not s.isnumeric()])

    if len(symbols) > 0:
        return True

    return False


def get_part_nums(line):
    """
    Get the part number candidates removing symbols and storing the index.

    Args:
        line (string)
            The line to parse.

    Returns:
        ndarray
            A list of indices.
        list
            A list of the parsed part numbers.
    """
    part_nums = []
    part_inds = []
    pnum = None
    for j, s in enumerate(line):
        if s.isnumeric() and pnum is None:
            pnum = s
            ind = j
        elif s.isnumeric():
            pnum += s
        elif pnum is not None:
            part_nums.append(pnum)
            part_inds.append(ind)
            pnum = None
    if pnum is not None:
        part_nums.append(pnum)
        part_inds.append(ind)

    return part_inds, part_nums


fpath = sys.argv[1]

with open(fpath, "r") as f:
    # Read the file into a list without newlines
    lines = f.read().split("\n")

# Part 1

# Initialise a sum
result = 0

# Loop over lines
for i, line in enumerate(lines):
    # Get the part number candidates removing symbols and storing the index
    part_inds, part_nums = get_part_nums(line)

    # Loop over part numbers
    for ind, pnum in zip(part_inds, part_nums):
        # Initialise flag
        add_num = False

        # Check for surrounding symbols
        if contains_symbols(line, ind, len(pnum) + 1):
            add_num = True

        # Check above (including diagonals)
        if i > 0:
            if contains_symbols(lines[i - 1], ind, len(pnum) + 1):
                add_num = True

        # Check below
        if i + 1 < len(lines):
            if contains_symbols(lines[i + 1], ind, len(pnum) + 1):
                add_num = True

        if add_num:
            result += int(pnum)

print("Part 1:", result)

# Part 2

# Initialise a sum
result = 0

# Loop over lines
for i, line in enumerate(lines):
    # Get the part number candidates removing symbols and storing the index for
    # this line and the surrounding lines
    part_inds, part_nums = get_part_nums(line)
    if i > 0:
        above_inds, above_nums = get_part_nums(lines[i - 1])
    else:
        above_inds, above_nums = None, None
    if i + 1 < len(lines):
        below_inds, below_nums = get_part_nums(lines[i + 1])
    else:
        below_inds, below_nums = None, None

    # Get the gear positions
    gear_inds = [i for i in range(len(line)) if line[i] == "*"]

    # Skip lines without gears
    if len(gear_inds) == 0:
        continue

    # Loop over gear positions
    for ind in gear_inds:
        # Initialise candidate list
        candidate_gears = []

        # Initialise dist list
        dists = []

        # Get the distance to part_numbers on the same line
        for pnum_ind, pnum in zip(part_inds, part_nums):
            candidate_gears.append(int(pnum))

            # Get the minimum character distance
            char_dists = np.zeros(len(pnum))
            for j, char in enumerate(pnum):
                char_dists[j] = abs(pnum_ind + j - ind)
            dists.append(np.min(char_dists))

        # Get the distance to part_numbers on the line above
        for pnum_ind, pnum in zip(above_inds, above_nums):
            candidate_gears.append(int(pnum))

            # Get the minimum character distance
            char_dists = np.zeros(len(pnum))
            for j, char in enumerate(pnum):
                char_dists[j] = abs(pnum_ind + j - ind)
            dists.append(np.min(char_dists))

        # Get the distance to part_numbers on the line below
        for pnum_ind, pnum in zip(below_inds, below_nums):
            candidate_gears.append(int(pnum))

            # Get the minimum character distance
            char_dists = np.zeros(len(pnum))
            for j, char in enumerate(pnum):
                char_dists[j] = abs(pnum_ind + j - ind)
            dists.append(np.min(char_dists))

        # Convert to arrays
        candidate_gears = np.array(candidate_gears)
        dists = np.array(dists)

        # Remove candidates that aren't adjacent
        okinds = dists < 2
        dists = dists[okinds]
        gear_ratio = candidate_gears[okinds]

        # Combine gears
        if len(gear_ratio) == 2:
            result += gear_ratio[0] * gear_ratio[1]

print("Part 2:", result)
