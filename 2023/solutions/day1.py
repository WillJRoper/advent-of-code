"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to
take a look. The Elves have even given you a map; on it, they've used stars to
mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations,
you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete
the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful
enough") and where they're even sending you ("the sky") and why your map looks
mostly blank ("you sure ask a lot of questions") and hang on did you just say
the sky ("of course, where do you think snow comes from") when you realize that
the Elves are already loading you into a trebuchet ("please hold still, we need
to strap you in").

As they're making the final adjustments, they discover that their calibration
document (your puzzle input) has been amended by a very young Elf who was
apparently just excited to show off her art skills. Consequently, the Elves
are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line
originally contained a specific calibration value that the Elves now need to
recover. On each line, the calibration value can be found by combining the
first digit and the last digit (in that order) to form a single two-digit
number.

For example:

 wc1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15,
and 77. Adding these together produces 142.

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: one, two, three, four, five, six, seven,
 eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and
last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.
"""
import sys


# Get file to open
fpath = sys.argv[1]

# Set up result
result = 0

# Open the file
with open(fpath, "r") as f:
    # Loop line by line
    for line in f:
        # Define new line for moving forward
        forward_line = line

        # Replace word numbers with numeric numbers starting from the start
        for ind in range(len(line)):
            subset = forward_line[ind : ind + 5]
            subset = (
                subset.replace("one", "1")
                .replace("two", "2")
                .replace("three", "3")
            )
            subset = (
                subset.replace("four", "4")
                .replace("five", "5")
                .replace("six", "6")
            )
            subset = (
                subset.replace("seven", "7")
                .replace("eight", "8")
                .replace("nine", "9")
            )
            forward_line = (
                forward_line[:ind] + subset + forward_line[ind + 5 :]
            )

            # If we've changed the line we found the first number and can stop
            if forward_line != line:
                break

        # Get the first digit
        for char in forward_line:
            # Exit at first number
            if char.isnumeric():
                first = char
                break

        # Define new line for moving backwards
        backward_line = line

        # Replace word numbers with numeric numbers starting from the end
        # (with some overspill)
        for ind in range(len(line), -1, -1):
            subset = backward_line[ind : ind + 5]
            subset = (
                subset.replace("one", "1")
                .replace("two", "2")
                .replace("three", "3")
            )
            subset = (
                subset.replace("four", "4")
                .replace("five", "5")
                .replace("six", "6")
            )
            subset = (
                subset.replace("seven", "7")
                .replace("eight", "8")
                .replace("nine", "9")
            )
            backward_line = (
                backward_line[:ind] + subset + backward_line[ind + 5 :]
            )

            # If we've changed the line we found the first number and can stop
            if backward_line != line:
                break

        # Get the last digit
        for char in backward_line[::-1]:
            # Exit at first number
            if char.isnumeric():
                last = char
                break

        # Combine them to a single integer
        num = int(first + last)

        # Add this number to the result
        result += num

print(result)
