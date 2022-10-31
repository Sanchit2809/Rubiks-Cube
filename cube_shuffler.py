
from cube_structure import *
from cube_moves import *
from random import randint , choice 


def shuffle(cube, lower_bound = 5, upper_bound = 100):
        moves = randint(lower_bound, upper_bound)
        actions = [
            ('h', 0),
            ('h', 1),
            ('v', 0),
            ('v', 1),
            ('s', 0),
            ('s', 1)
        ]
        for i in range(moves):
            a = choice(actions)
            j = randint(0, cube.n - 1)
            if a[0] == 'h':
                print("operation-",a,"row no - ",j)
                #print("row no - ",j)
                horizontal(cube,j, a[1])
                
            elif a[0] == 'v':
                print("operation-",a,"column no -",j)
                vertical(cube,j, a[1])
                #print("column no -",j)
            elif a[0] == 's':
                print("operation-",a,"column no -",j)
                top_side(cube,j, a[1])
                #print("column no -",j)