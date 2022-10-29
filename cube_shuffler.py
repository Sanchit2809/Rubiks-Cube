
from cube_structure import RubiksCube 

from cube_moves import horiontal,vertical 

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
            j = randint(0, objct.n - 1)
            if a[0] == 'h':
                objct.horizontal(j, a[1])
            elif a[0] == 'v':
                objct.vertical(j, a[1])
            elif a[0] == 's':
                objct.side(j, a[1])