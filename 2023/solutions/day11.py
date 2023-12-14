"""
--- Day 11: Cosmic Expansion ---
You continue following signs for "Hot Springs" and eventually come across an
observatory. The Elf within turns out to be a researcher studying cosmic
expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting
for this research project. However, he confirms that the hot springs are the
next-closest area likely to have people; he'll even take you straight there
once he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a
single giant image (your puzzle input). The image includes empty space (.)
and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

The researcher is trying to figure out the sum of the lengths of the shortest
path between every pair of galaxies. However, there's a catch: the universe
expanded in the time it took the light from those galaxies to reach the
observatory.

Due to something involving gravitational effects, only some space expands.
In fact, the result is that any rows or columns that contain no galaxies
should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
These rows and columns need to be twice as big; the result of cosmic expansion
therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
Equipped with this expanded universe, the shortest path between every pair of
galaxies can be found. It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
In these 9 galaxies, there are 36 pairs. Only count each pair once; order
within the pair doesn't matter. For each pair, find any shortest path between
the two galaxies using only steps that move up, down, left, or right exactly
one . or # at a time. (The shortest path between two galaxies is allowed to
pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......
This path has length 9 because it takes a minimum of nine steps to get from
galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy
9 itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5
In this example, after expanding the universe, the sum of the shortest path
between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every
pair of galaxies. What is the sum of these lengths?

--- Part Two ---

The galaxies are much older (and thus much farther apart) than the researcher
initially estimated.

Now, instead of the expansion you did before, make each empty row or column
one million times larger. That is, each empty row should be replaced with
1000000 empty rows, and each empty column should be replaced with 1000000
empty columns.

(In the example above, if each empty row or column were merely 10 times
larger, the sum of the shortest paths between every pair of galaxies would
be 1030. If each empty row or column were merely 100 times larger, the sum of
the shortest paths between every pair of galaxies would be 8410. However, your
universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these
new rules, then find the length of the shortest path between every pair of
galaxies. What is the sum of these lengths?
"""
import sys
import numpy as np
import itertools


# Get the file path
fpath = sys.argv[1]

# Open the file
with open(fpath, "r") as f:
    lines = f.read().strip().split("\n")

# Part 1

# Convert the input to a numpy array
arr = np.zeros((len(lines), len(lines[0])))
ngal = 1
for i, line in enumerate(lines):
    for j, char in enumerate(lines[i]):
        if char == "#":
            arr[i, j] = ngal
            ngal += 1

# Find the empty rows
empty_rows = []
for i in range(arr.shape[0]):
    if np.sum(arr[i, :]) == 0:
        empty_rows.append(i)

# Find the empty columns
empty_cols = []
for j in range(arr.shape[1]):
    if np.sum(arr[:, j]) == 0:
        empty_cols.append(j)

# Expand the universe! (Backwards so the indices don't need modifying)
for row in empty_rows[::-1]:
    arr = np.insert(arr, row, np.zeros(arr.shape[1]), axis=0)
for col in empty_cols[::-1]:
    arr = np.insert(arr, col, np.zeros(arr.shape[0]), axis=1)

# Get the coordinates of each galaxy and count them
coords = np.zeros((ngal, 2), dtype=int)
ngal = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i, j] > 0:
            coords[ngal, 0] = i
            coords[ngal, 1] = j
            ngal += 1

# Define all combinations (in terms of coordinate index)
pairs = itertools.combinations(range(0, ngal), 2)


def shortest_path(coord1, coord2):
    return np.sum(np.abs(coord1 - coord2))


# Find the distance between all. Only up, down, left and right is allowed
# which is the same as moving all of them at once in a right angle
shortest_sum = 0
for pair in pairs:
    shortest_sum += shortest_path(coords[pair[0]], coords[pair[1]])

print("Part 1", shortest_sum)

# Part 2 -> no explicit expansion this time, we'll add it on after wards

# Convert the input to a numpy array
arr = np.zeros((len(lines), len(lines[0])))
ngal = 1
for i, line in enumerate(lines):
    for j, char in enumerate(lines[i]):
        if char == "#":
            arr[i, j] = ngal
            ngal += 1

# Find the empty rows
empty_rows = []
for i in range(arr.shape[0]):
    if np.sum(arr[i, :]) == 0:
        empty_rows.append(i)

# Find the empty columns
empty_cols = []
for j in range(arr.shape[1]):
    if np.sum(arr[:, j]) == 0:
        empty_cols.append(j)
print(empty_rows, empty_cols)
# Get the coordinates of each galaxy and count them
coords = np.zeros((ngal, 2), dtype=int)
ngal = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i, j] > 0:
            coords[ngal, 0] = i
            coords[ngal, 1] = j
            ngal += 1

# Define all combinations (in terms of coordinate index)
pairs = itertools.combinations(range(0, ngal), 2)


def shortest_path_with_expansion(
    coord1,
    coord2,
    empty_rows,
    empty_cols,
    nexpand,
):
    # Ridiculous subtract 1 to get the right answer
    nexpand -= 1

    # Calculate the unexpanded distance
    dist = np.sum(np.abs(coord1 - coord2))

    # Get the minimum and maximum row and column
    min_row = np.min([coord1[0], coord2[0]])
    max_row = np.max([coord1[0], coord2[0]])
    min_col = np.min([coord1[1], coord2[1]])
    max_col = np.max([coord1[1], coord2[1]])

    # How many empty rows are there in between these galaxies?
    for row in range(min_row + 1, max_row):
        if row in empty_rows:
            dist += nexpand

    # How many empty coloumns are there in between these galaxies?
    for col in range(min_col + 1, max_col):
        if col in empty_cols:
            dist += nexpand

    return dist


# Find the distance between all, same as before but now more expansion
shortest_sum = 0
for pair in pairs:
    shortest_sum += shortest_path_with_expansion(
        coords[pair[0]], coords[pair[1]], empty_rows, empty_cols, nexpand=1000000
    )

print("Part 2", shortest_sum)
