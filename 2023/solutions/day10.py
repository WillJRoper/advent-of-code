"""
--- Day 10: Pipe Maze ---
You use the hang glider to ride the hot air from Desert Island all the way up
to the floating metal island. This island is surprisingly cold and there
definitely aren't any thermals to glide on, so you leave your hang glider
behind.

You wander around for a while, but you don't find any people or animals.
However, you do occasionally find signposts labeled "Hot Springs" pointing in
a seemingly consistent direction; maybe you can find someone at the hot springs
and ask them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As
you stop to admire some metal grass, you notice something metallic scurry away
in your peripheral vision and jump into a big pipe! It didn't look like any
animal you've ever seen; if you want a better look, you'll need to get ahead
of it.

Scanning the area, you discover that the entire field you're standing on is
densely packed with pipes; it was hard to tell at first because they're the
same metallic silver color as the "ground". You make a quick sketch of all of
the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but
your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe
that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....
If the animal had entered this loop in the northwest corner, the sketch would
instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....
In the above diagram, the S tile is still a 90-degree F bend: you can tell
because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop!
This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF
In the above diagram, you can still figure out which pipes form the main loop:
they're the ones connected to S, pipes those pipes connect to, pipes those
pipes connect to, and so on. Every pipe in the main loop connects to its two
neighbors (including S, which will have exactly two pipes connecting to it,
and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles
also shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the
loop that is farthest from the starting position. Because the animal is in
the pipe, it doesn't make sense to measure this by direct distance. Instead,
you need to find the tile that would take the longest number of steps along
the loop to reach from the starting point - regardless of which way around
the loop the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....
You can count the distance each tile in the loop is from the starting point
like this:

.....
.012.
.1.3.
.234.
.....
In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...
Find the single giant loop starting at S. How many steps along the loop does
it take to get from the starting position to the point farthest from the
starting position?

--- Part Two ---

You quickly reach the farthest point of the loop, but the animal never emerges.
Maybe its nest is within the area enclosed by the loop?

To determine whether it's even worth taking the time to search for such a nest,
you should calculate how many tiles are contained within the loop. For example:

...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
The above loop encloses merely four tiles - the two pairs of . in the southwest
and southeast (marked I below). The middle . tiles (marked O below) are not in
the loop. Here is the same loop again with those regions marked:

...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....
In fact, there doesn't even need to be a full tile path to the outside for
tiles to count as outside the loop - squeezing between pipes is also allowed!
Here, I is still within the loop and O is still outside the loop:

..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
In both of the above examples, 4 tiles are enclosed by the loop.

Here's a larger example:

.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
The above sketch has many random bits of ground, some of which are in the
loop (I) and some of which are outside it (O):

OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
In this larger example, 8 tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the
loop. Here's another example with many bits of junk pipe lying around that
aren't connected to the main loop at all:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
Here are just the tiles that are enclosed by the loop marked with I:

FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
In this last example, 10 tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the
area within the loop. How many tiles are enclosed by the loop?
"""
import sys
import numpy as np
import matplotlib.pyplot as plt


class Pipe:
    def __init__(self, coord, pipe, grid_shape):
        # Store pipe and position
        self.coord = coord
        self.pipe = pipe

        # Define and get connections
        self.connections = None
        self._connections()

        # Intialise the links
        self.prev = None
        self.next = None

        # Intialise the step in the path
        self.step = -1

        # Store the shape of the grid for convinience
        self.grid_shape = grid_shape

    def _connections(self):
        """
        Get the directions this pipe can
        """

        # Define the connection directions
        match self.pipe:
            case "|":
                self.outs = {"north", "south"}
                self.ins = {"south", "north"}
            case "-":
                self.outs = {"east", "west"}
                self.ins = {"west", "east"}
            case "L":
                self.outs = {"north", "east"}
                self.ins = {"south", "west"}
            case "J":
                self.outs = {"north", "west"}
                self.ins = {"south", "east"}
            case "7":
                self.outs = {"south", "west"}
                self.ins = {"north", "east"}
            case "F":
                self.outs = {"south", "east"}
                self.ins = {"north", "west"}
            case _:
                return

    def link(self, grid):
        """
        Finds and stores the links between currounding pipes.
        """

        # Handle different pipes
        match self.pipe:
            case "|":
                self.prev = tuple(self.coord + np.array([-1, 0]))
                self.next = tuple(self.coord + np.array([1, 0]))
            case "-":
                self.prev = tuple(self.coord + np.array([0, 1]))
                self.next = tuple(self.coord + np.array([0, -1]))
            case "L":
                self.prev = tuple(self.coord + np.array([-1, 0]))
                self.next = tuple(self.coord + np.array([0, 1]))
            case "J":
                self.prev = tuple(self.coord + np.array([-1, 0]))
                self.next = tuple(self.coord + np.array([0, -1]))
            case "7":
                self.prev = tuple(self.coord + np.array([1, 0]))
                self.next = tuple(self.coord + np.array([0, -1]))
            case "F":
                self.prev = tuple(self.coord + np.array([1, 0]))
                self.next = tuple(self.coord + np.array([0, 1]))
            case _:
                return

        # Handle any ill defined coordinates
        if self.prev[0] < 0:
            self.prev = None
        elif self.prev[0] > self.grid_shape[0] - 1:
            self.prev = None
        elif self.prev[1] < 0:
            self.prev = None
        elif self.prev[1] > self.grid_shape[1] - 1:
            self.prev = None
        if self.next[0] < 0:
            self.next = None
        elif self.next[0] > self.grid_shape[0] - 1:
            self.next = None
        elif self.next[1] < 0:
            self.next = None
        elif self.next[1] > self.grid_shape[1] - 1:
            self.next = None

        # Convert the tuple to the pipe object
        self.prev = None if self.prev is None else grid[self.prev]
        self.next = None if self.next is None else grid[self.next]

        # Sanitise the links for only pipes that can actually connect
        if self.prev is not None and len(self.outs - self.prev.ins) == len(self.outs):
            self.prev = None
        if self.next is not None and len(self.outs - self.next.ins) == len(self.outs):
            self.next = None

    def __str__(self):
        """
        Print overload for debugging.
        """
        return f"< {self.pipe} @ {self.coord} with step = {self.step} >"


# Get the file path
fpath = sys.argv[1]

# Open the file
with open(fpath, "r") as f:
    lines = f.read().strip().split("\n")

# Get the grid shape
grid_shape = (len(lines), len(lines[0]))

# Define an array to store the pipe grid
grid = np.empty(grid_shape, dtype=object)

# Populate the grid and find the starting coordinates
for i in range(grid_shape[0]):
    for j in range(grid_shape[1]):
        if lines[i][j] == ".":
            grid[i, j] = None
            continue

        # Get and set the start node step and coord
        if lines[i][j] == "S":
            start = (i, j)
            # Create the pipe
            grid[i, j] = Pipe(np.array([i, j]), "|", grid_shape)
            grid[i, j].step = 0
        else:
            # Create the pipe
            grid[i, j] = Pipe(np.array([i, j]), lines[i][j], grid_shape)

# Construct all links in the doubley linked lists
for i in range(grid_shape[0]):
    for j in range(grid_shape[1]):
        pipe = grid[i, j]

        if pipe is not None:
            pipe.link(grid)

# Get the initial pipes
current_pipes = [grid[start]]

# Define a grid to store the steps
steps_grid = np.full(grid_shape, np.nan)
steps_grid[start] = 0

plt.figure(figsize=(6, 6))

# Walk the pipe network
while len(current_pipes) > 0:
    # Loop over the current pipes
    next_pipes = []
    for pipe in current_pipes:
        # Store the steps
        steps_grid[pipe.coord[0], pipe.coord[1]] = pipe.step
        prev_pipe = pipe

        # Update the previous and next pipes
        if pipe.prev is not None and pipe.prev.step == -1:
            pipe.prev.step = pipe.step + 1
            pipe = pipe.prev
        elif pipe.next is not None and pipe.next.step == -1:
            pipe.next.step = pipe.step + 1
            pipe = pipe.next
        else:
            pipe = None

        # Skip pipeless cells
        if pipe is None:
            continue

        # Add the pipe to the set for searching
        next_pipes.append(pipe)

        plt.plot(
            (prev_pipe.coord[0] + 0.5, pipe.coord[0] + 0.5),
            (prev_pipe.coord[1] + 0.5, pipe.coord[1] + 0.5),
            color="k",
            zorder=1,
        )

    # Move to the next step
    current_pipes = next_pipes

print("Part 1:", np.ceil(np.nanmax(steps_grid) / 2))

end = np.where(steps_grid == np.ceil(np.nanmax(steps_grid) / 2))

plt.imshow(
    steps_grid.T,
    extent=[0, grid_shape[0], 0, grid_shape[1]],
    origin="lower",
    zorder=0,
)
plt.scatter(
    (start[0] + 0.5, end[0][0] + 0.5),
    (start[1] + 0.5, end[1][0] + 0.5),
    marker="*",
    color="orange",
    zorder=2,
)
plt.show()

# Part 2


def calculate_polygon_area(vertices):
    n = len(vertices)

    if n < 3:
        # A polygon must have at least 3 vertices
        return 0.0

    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]

        area += x1 * y2 - x2 * y1

    area = abs(area) / 2.0

    return area


# We need to redo part 1 but find the vertices of tiles in the loop
vertices = []

# Define an array to store the pipe grid
grid = np.empty(grid_shape, dtype=object)

# Populate the grid and find the starting coordinates
for i in range(grid_shape[0]):
    for j in range(grid_shape[1]):
        if lines[i][j] == ".":
            grid[i, j] = None
            continue

        # Get and set the start node step and coord
        if lines[i][j] == "S":
            start = (i, j)
            # Create the pipe
            grid[i, j] = Pipe(np.array([i, j]), "|", grid_shape)
            grid[i, j].step = 0
        else:
            # Create the pipe
            grid[i, j] = Pipe(np.array([i, j]), lines[i][j], grid_shape)

# Construct all links in the doubley linked lists
for i in range(grid_shape[0]):
    for j in range(grid_shape[1]):
        pipe = grid[i, j]

        if pipe is not None:
            pipe.link(grid)

# Get the initial pipes
current_pipes = [grid[start]]

# Define a grid to store the steps
steps_grid = np.full(grid_shape, np.nan)
steps_grid[start] = 0

# Walk the pipe network
while len(current_pipes) > 0:
    # Loop over the current pipes
    next_pipes = []
    for pipe in current_pipes:
        # Store the steps
        steps_grid[pipe.coord[0], pipe.coord[1]] = pipe.step
        prev_pipe = pipe

        vertices.append(pipe.coord)

        # Update the previous and next pipes
        if pipe.prev is not None and pipe.prev.step == -1:
            pipe.prev.step = pipe.step + 1
            pipe = pipe.prev
        elif pipe.next is not None and pipe.next.step == -1:
            pipe.next.step = pipe.step + 1
            pipe = pipe.next
        else:
            pipe = None

        # Skip pipeless cells
        if pipe is None:
            continue

        # Add the pipe to the set for searching
        next_pipes.append(pipe)

        plt.plot(
            (prev_pipe.coord[0] + 0.5, pipe.coord[0] + 0.5),
            (prev_pipe.coord[1] + 0.5, pipe.coord[1] + 0.5),
            color="k",
            zorder=1,
        )

    # Move to the next step
    current_pipes = next_pipes

# Calculate the area
area = calculate_polygon_area(vertices)
print("Part 2:", area - np.ceil(np.nanmax(steps_grid) / 2) + 1)
