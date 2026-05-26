"""
Dungeon Master 2D

You are trapped in a 2D maze and need to find the quickest way out! The maze is
composed of unit squares which may or may not be filled with rock. It takes one
minute to move one unit north, south, east, or west. You cannot move diagonally
and the maze is surrounded by solid rock on all sides.

Is an escape possible? If yes, how long will it take?

Key Constraints
    - 4 movement directions: N, S, E, W
    - Grid size up to 30x30
    - Multiple test cases, terminated by 0 0
    - Exactly one S and one E per maze

Input Specification
The input consists of a number of mazes. Each maze description starts with a line
containing two integers R and C (both limited to 30). R is the number of rows and
C is the number of columns.

Then follow R lines each containing C characters. Each character describes one cell:

    #  rock (blocked)
    .  empty (passable)
    S  your starting position
    E  the exit

There is a single blank line after each maze. Input is terminated by 0 0.


Output Specification
Each maze generates one line of output.

    Escape possible:  Escaped in X minute(s).
    No escape:        Trapped!


Sample Input
4 4
S...
.##.
.##.
...E

3 3
S##
###
##E

0 0


Sample Output
Escaped in 6 minute(s).
Trapped!

"""