"""
--- Day 8: Haunted Wasteland ---
You're still riding a camel across Desert Island when you spot a sandstorm
quickly approaching. When you turn to warn the Elf, she disappears before your
eyes! To be fair, she had just finished warning you about ghosts a few minutes
ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of
documents (your puzzle input) about how to navigate the desert. At least,
you're pretty sure that's what they are; one of the documents contains a list
of left/right instructions, and the rest of the documents seem to describe
some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate
the network. Perhaps if you have the camel follow the same instructions, you
can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel
like AAA is where you are now, and you have to follow the left/right
instructions until you reach ZZZ.

This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)

Starting with AAA, you need to look up the next element based on the next
left/right instruction in your input. In this example, start with AAA and
go right (R) by choosing the right element of AAA, CCC. Then, L means to
choose the left element of CCC, ZZZ. By following the left/right instructions,
you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right
instructions, repeat the whole sequence of instructions as necessary: RL
really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation
that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

Starting at AAA, follow the left/right instructions. How many steps are
required to reach ZZZ?
"""
import sys
import math

# Part 1

# Get the file path
fpath = sys.argv[1]

# Open the file
with open(fpath, "r") as f:
    lines = f.read().split("\n")

# Get the left/right instructions
insts = lines[0]

# Create a dictionary to store the directions
directions = {}

# Populate the directions dict
for line in lines[1:]:
    if len(line) == 0:
        continue

    # Get the key
    key = line.split("=")[0].strip()

    # Get the left and right directions
    left, right = (
        line.split("=")[-1].replace("(", "").replace(")", "").strip().split(", ")
    )

    # Store these
    directions[key] = {"L": left, "R": right}

# Loop until we teach the end
pos = "AAA"
nsteps = 0
while pos != "ZZZ":
    # Get next instruction
    pos = directions[pos][insts[nsteps % len(insts)]]
    nsteps += 1

print("Part 1:", nsteps)

# Part 2

# Get the file path
fpath = sys.argv[2 if len(sys.argv) > 2 else 1]

# Open the file
with open(fpath, "r") as f:
    lines = f.read().split("\n")

# Get the left/right instructions
insts = lines[0]

# Create a dictionary to store the directions
directions = {}

# Get all starts
starts = []
for line in lines[1:]:
    if len(line) == 0:
        continue
    if line[2] == "A":
        starts.append(line[:3])
print(starts)

# Populate the directions dict
for line in lines[1:]:
    if len(line) == 0:
        continue

    # Get the key
    key = line.split("=")[0].strip()

    # Get the left and right directions
    left, right = (
        line.split("=")[-1].replace("(", "").replace(")", "").strip().split(", ")
    )

    # Store these
    directions[key] = {"L": left, "R": right}

# Loop until we reach the end for each start
poss = starts
ends = []
nsteps = 0
while len(poss) > 0:
    # Get next set of instructions
    new_poss = []
    for pos in poss:
        new_poss.append(directions[pos][insts[nsteps % len(insts)]])
    poss = new_poss
    nsteps += 1

    for pos in poss:
        if pos[2] == "Z":
            ends.append(nsteps)
            poss.remove(pos)

print(ends)

print("Part 2:", math.lcm(*ends))
