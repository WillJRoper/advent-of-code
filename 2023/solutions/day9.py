"""
--- Day 9: Mirage Maintenance ---
You ride the camel through the sandstorm and stop where the ghost's maps told
you to stop. The sandstorm subsequently subsides, somehow seeing you standing
at an oasis!

The camel goes to get some water and you stretch your neck. As you look up,
you discover what must be yet another giant floating island, this one made
of metal! That must be where the parts to fix the sand machines come from.

There's even a hang glider partially buried in the sand here; once the sun
rises and heats up the sand, you might be able to use the glider and the hot
air to get all the way up to the metal island!

While you wait for the sun to rise, you admire the oasis hidden here in the
middle of Desert Island. It must have a delicate ecosystem; you might as well
take some ecological readings while you wait. Maybe you can report any
environmental instabilities you find to someone so the oasis can be around
for the next sandstorm-worn traveler.

You pull out your handy Oasis And Sand Instability Sensor and analyze your
surroundings. The OASIS produces a report of many values and how they are
changing over time (your puzzle input). Each line in the report contains
the history of a single value. For example:

0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
To best protect the oasis, your environmental report should include a
prediction of the next value in each history. To do this, start by making a
new sequence from the difference at each step of your history. If that sequence
is not all zeroes, repeat this process, using the sequence you just generated
as the input sequence. Once all of the values in your latest sequence are
zeroes, you can extrapolate what the next value of the original history
should be.

In the above dataset, the first history is 0 3 6 9 12 15. Because the
values increase by 3 each step, the first sequence of differences that you
generate will be 3 3 3 3 3. Note that this sequence has one fewer value than
the input sequence because at each step it considers two numbers from the
input. Since these values aren't all zero, repeat the process: the values
differ by 0 at each step, so the next sequence is 0 0 0 0. This means you have
enough information to extrapolate the history! Visually, these sequences can
be arranged like this:

0   3   6   9  12  15
  3   3   3   3   3
    0   0   0   0
To extrapolate, start by adding a new zero to the end of your list of zeroes;
because the zeroes represent differences between the two values above them,
this also means there is now a placeholder in every sequence above it:

0   3   6   9  12  15   B
  3   3   3   3   3   A
    0   0   0   0   0
You can then start filling in placeholders from the bottom up. A needs to be
the result of increasing 3 (the value to its left) by 0 (the value below it);
this means A must be 3:

0   3   6   9  12  15   B
  3   3   3   3   3   3
    0   0   0   0   0
Finally, you can fill in B, which needs to be the result of increasing 15
(the value to its left) by 3 (the value below it), or 18:

0   3   6   9  12  15  18
  3   3   3   3   3   3
    0   0   0   0   0
So, the next value of the first history is 18.

Finding all-zero differences for the second history requires an
additional sequence:

1   3   6  10  15  21
  2   3   4   5   6
    1   1   1   1
      0   0   0
Then, following the same process as before, work out the next value in
each sequence from the bottom up:

1   3   6  10  15  21  28
  2   3   4   5   6   7
    1   1   1   1   1
      0   0   0   0
So, the next value of the second history is 28.

The third history requires even more sequences, but its next value can be
found the same way:

10  13  16  21  30  45  68
   3   3   5   9  15  23
     0   2   4   6   8
       2   2   2   2
         0   0   0
So, the next value of the third history is 68.

If you find the next value for each history in this example and add them
together, you get 114.

Analyze your OASIS report and extrapolate the next value for each history.
What is the sum of these extrapolated values?

--- Part Two ---
Of course, it would be nice to have even more history included in your report.
Surely it's safe to just extrapolate backwards as well, right?

For each history, repeat the process of finding differences until the sequence
of differences is entirely zero. Then, rather than adding a zero to the end
and filling in the next values of each previous sequence, you should instead
add a zero to the beginning of your sequence of zeroes, then fill in new first
values for each previous sequence.

In particular, here is what the third example history looks like when
extrapolating back in time:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0

Adding the new values on the left side of each sequence from bottom to top
eventually reveals the new left-most history value: 5.

Doing this for the remaining example data above results in previous values of
-3 for the first history and 0 for the second history. Adding all three new
values together produces 2.

Analyze your OASIS report again, this time extrapolating the previous value
for each history. What is the sum of these extrapolated values?
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colormaps
from matplotlib.colors import LogNorm
from scipy.interpolate import interp1d


# Part 1

# Get the file path
fpath = sys.argv[1]

# Open the file
with open(fpath, "r") as f:
    lines = f.read().split("\n")

# Convert lines to lists of integers
lines = [
    np.array([int(i) for i in line.strip().split(" ")])
    for line in lines
    if len(line) > 0
]


def recursive_predict(line):
    """
    Recursively calculate differences between terms and find the next term
    in the sequence.
    """

    # If we haven't reached the bottom (all zeros) calculate the difference
    # of terms and recurse, the return will be the next term
    next_term = 0
    if not (sum(line) == 0 and np.unique(line).size == 1):
        next_term = recursive_predict(line[1:] - line[:-1])

    return line[-1] + next_term


# Define the result to be added to
result = 0

# Loop over lines
for line in lines:
    # Recursively find the next term
    result += recursive_predict(line)

print("Part 1:", result)


# Part 2


def recursive_history(line):
    """
    Recursively calculate differences between terms and find the first term
    in the sequence.
    """

    # If we haven't reached the bottom (all zeros) calculate the difference
    # of terms and recurse, the return will be the first term
    first_term = 0
    if not (sum(line) == 0 and np.unique(line).size == 1):
        first_term = recursive_history(line[1:] - line[:-1])

    return line[0] - first_term


# Define the result to be added to
result = 0

# Loop over lines
for line in lines:
    # Recursively find the next term
    result += recursive_history(line)

print("Part 2:", result)

# Make a pretty plot
data = {}


def recursive_both(line, data):
    """
    Recursively calculate differences between terms and find the first term
    in the sequence.
    """

    # If we haven't reached the bottom (all zeros) calculate the difference
    # of terms and recurse, the return will be the first term
    first_term = 0
    next_term = 0
    if not (sum(line) == 0 and np.unique(line).size == 1):
        first_term, next_term = recursive_both(line[1:] - line[:-1], data)

    new_line = list(line)
    new_line.insert(0, first_term)
    new_line.append(next_term)

    data.setdefault("lines", []).append(new_line)

    return line[0] - first_term, line[-1] + next_term


# Loop over lines
result1, result2 = 0, 0
for i, line in enumerate(lines):
    # Recursively find the next term
    first_term, next_term = recursive_both(line, data.setdefault(i, {}))
    result2 += first_term
    result1 += next_term

print("Combined:", result1, result2)

# Construct plot behaviour
xs = []
ys = []
colors = []
nline = 0
for key in list(data.keys())[:100]:
    for line in data[key]["lines"]:
        for n, val in enumerate(line):
            nline += 1
            xs.append(nline)
            ys.append(val)
            colors.append(n)

xs = np.array(xs)
ys = np.array(ys)
colors = np.array(colors)

# Create a colormap
cmap = colormaps["plasma"]

# Normalize data to the range [0, 1] for colormap mapping
normalize = plt.Normalize(min(colors), max(colors))

ys_func = interp1d(xs, ys, kind="cubic")
colors_func = interp1d(xs, colors, kind="linear")

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
for i in range(len(xs) - 1):
    new_xs = np.linspace(xs[i], xs[i + 1], 10)
    for j in range(10):
        ax.plot(
            new_xs[j : j + 2],
            np.arcsinh(ys_func(new_xs[j : j + 2])),
            color=cmap(normalize(colors_func(new_xs[j]))),
        )
ax.axis(False)
plt.show()
