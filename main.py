from cube_structure import *
from cube_display import *
from cube_shuffler import *
from cube_moves import *
from solved_checker import solved


cube = RubiksCube(n=3)
show(cube)
check = solved(cube)
print(check)

shuffle(cube)
show(cube)
check = solved(cube)
print(check)