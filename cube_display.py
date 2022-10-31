from cube_structure import *
def show(cube):
    spacing = f'{" " * (len(str(cube.struct[0][0])) + 2)}'
    l1 = '\n'.join(spacing + str(c) for c in cube.struct[0])
    l2 = '\n'.join('  '.join(str(cube.struct[i][j]) for i in range(1,5)) for j in range(len(cube.struct[0])))
    l3 = '\n'.join(spacing + str(c) for c in cube.struct[5])
    print(f'{l1}\n\n{l2}\n\n{l3}')
    
