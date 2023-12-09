"""--- Day 5: If You Give A Seed A Fertilizer ---
You take the boat and find the gardener right where you were told he would be:
managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow
Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with!
Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand
soon; we only turned off the water a few days... weeks... oh no." His face
sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot
to check why we stopped getting more sand! There's a ferry leaving soon that is
headed over in that direction - it's much faster than your boat. Could you
please go check it out?"

You barely have time to agree to this request when he brings up another. "While
you wait for the ferry, maybe you can help us with our food production problem.
The latest Island Island Almanac just arrived and we're having trouble making
sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted.
It also lists what type of soil to use with each kind of seed, what type of
fertilizer to use with each kind of soil, what type of water to use with each
kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on
is identified with a number, but numbers are reused by each category - that is,
soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55,
and 13.

The rest of the almanac contains a list of maps which describe how to convert
numbers from a source category into numbers in a destination category. That is,
the section that starts with seed-to-soil map: describes how to convert a seed
number (the source) to a soil number (the destination). This lets the gardener
and his team know which soil to use with which seeds, which water to use with
which fertilizer, and so on.

Rather than list every source number and its corresponding destination number
one by one, the maps describe entire ranges of numbers that can be converted.
Each line within a map contains three numbers: the destination range start,
the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of
98, and a range length of 2. This line means that the source range starts at
98 and contains two values: 98 and 99. The destination range is the same
length, but it starts at 50, so its two values are 50 and 51. With this
information, you know that seed number 98 corresponds to soil number 50 and
that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48
values: 50, 51, ..., 96, 97. This corresponds to a destination range starting
at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53
corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination
number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers
looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, you can look up the soil number required for each
initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, so they'd
like to know the closest location that needs a seed. Using these maps, find the
lowest location number that corresponds to any of the initial seeds. To do this,
you'll need to convert each seed number through other categories until you can
find its corresponding location number. In this example, the corresponding
types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78,
humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42,
humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82,
humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34,
 humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial
seed numbers?

"""
import sys


# Get the file path
fpath = sys.argv[1]

# Open the file
with open(fpath, "r") as f:
    lines = f.read().split("\n")

# Part 1

# Get the seeds
seeds = [int(i) for i in lines[0].split(":")[-1].strip().split(" ")]


class Map:
    """
    Class containing the maps.
    """

    def __init__(self, dest, source, num):
        self.source_map = range(source, source + num)
        self.dest_offset = dest - source

    def is_in_source(self, val):
        if val in self.source_map:
            return True
        return False

    def get_dest(self, source):
        return source + self.dest_offset


# Define a list to hold the map order
map_order = []

# Loop over lines to get the maps
maps = {}
key = None
for line in lines[1:]:
    if ":" in line:
        key = line.replace(" map:", "")
        maps[key] = []
        map_order.append(key)
        continue

    if len(line) > 0:
        args = line.strip().split(" ")
        maps[key].append(Map(*[int(i) for i in args]))

# Define a list to store locations
locs = []

# Loop over seeds
for source in seeds:
    # Loop over map order
    for key in map_order:
        # Loop over maps
        for dest_map in maps[key]:
            if dest_map.is_in_source(source):
                dest = dest_map.get_dest(source)
                source = dest
                break

        # If destination is found then dest = source and the next iteration
        # will have source = dest so we don't need to do anything

    # Store the location
    locs.append(source)

print("Part 1:", min(locs))

# Part 2

# Get the seeds
seed_start = [seeds[i] for i in range(0, len(seeds), 2)]
seed_num = [seeds[i] for i in range(1, len(seeds), 2)]
seed_ranges = [range(i, i + j) for i, j in zip(seed_start, seed_num)]


class Map:
    """
    Class containing the maps.
    """

    def __init__(self, dest, source, num):
        self.source_map = range(source, source + num)
        self.dest_offset = dest - source

    def get_overlap(self, source_range):
        overlap = range(
            max(source_range.start, self.source_map.start),
            min(source_range.stop, self.source_map.stop),
        )
        return overlap

    def get_dest_ranges(self, overlap_range):
        overlap_range = range(
            overlap_range.start + self.dest_offset,
            overlap_range.stop + self.dest_offset,
        )
        return overlap_range


# Define a list to hold the map order
map_order = []

# Loop over lines to get the maps
maps = {}
key = None
for line in lines[1:]:
    if ":" in line:
        key = line.replace(" map:", "")
        maps[key] = []
        map_order.append(key)
        continue

    if len(line) > 0:
        args = line.strip().split(" ")
        maps[key].append(Map(*[int(i) for i in args]))

# Define a list to store locations
locs = []

# Initialise the source maps with the seed ranges
source_maps = [*seed_ranges]

# Loop over map order
for key in map_order:
    # Define destination list
    dest_maps = []

    # Loop over maps
    while len(source_maps) > 0:
        # Get the next source map
        source_map = source_maps.pop(0)

        # Flag for whether an overlap is found
        found_overlap = False

        # Lists of overlaps
        overlaps = []
        non_overlap = []

        # Loop over destination maps
        for dest_map in maps[key]:
            # Find overlap
            overlap = dest_map.get_overlap(source_map)
            if len(overlap) > 0:
                overlaps.append(overlap)

                # Calculate and store the non-overlaping parts of the map
                lower = range(source_map.start, overlap.start)
                if len(lower) > 0:
                    non_overlap.append(lower)
                upper = range(overlap.stop, source_map.stop)
                if len(upper) > 0:
                    non_overlap.append(upper)

                # Convert to destination maps
                dest_maps.append(dest_map.get_dest_ranges(overlap))
                found_overlap = True

        # No overlap: dest = source
        if not found_overlap:
            dest_maps.append(source_map)

        # Add the overlaps as sources for testing with other destination maps
        if len(non_overlap) > 0:
            source_maps.extend(non_overlap)

    # Next set of sources are this set of destinations
    source_maps = dest_maps

# Get the minimum of each location range
locs = [r.start for r in dest_maps]

print("Part 2:", min(locs))
