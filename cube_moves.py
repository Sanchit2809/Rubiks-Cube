def horiontal(cube , row , direction ):
    if row< len(cube.struct[0]):
'''
    first rotating the side faces then turning the upper and lower faces 
'''
    if row < len(cube.struct[0])
# side faces shift 
        # left -> direction == 0 
        if direction == 0 :
            cube.struct[1][row],cube.struct[2][row],cube.struct[3][row],cube.struct[4][row] = (cube.struct[2][row],cube.struct[3][row],cube.struct[4][row],cube.struct[1][row])
        # right -> direction == 1 
        elif direction == 1:
            cube.struct[1][row],cube.struct[2][row],cube.struct[3][row],cube.struct[4][row] = (cube.struct[4][row],cube.struct[1][row],cube.struct[2][row],cube.struct[3][row])
        else:
            printf("ERROR direction specified is not possible ")
            return 
# top and bottom faces rotated 
'''
since the top and bottom are only shifted when the row is either 0 or 2 we check the same while rotating the faces 
'''
        if direction == 0:
            if row == 0:
                cube.struct[0] = [list(x) for x in zip(*reversed(cube.struct[0]))]
            elif row == len(cube.struct[0])-1 :
                cube.struct[5] = [list(x) for x in zip(*reversed(cube.struct[5]))]
        elif direction == 1:
            if row == 0:
                cube.struct[0] = [list(x) for x in zip (*cube.struct[0])][::-1]
            elif row == len(cube.struct[0])-1 :
                cube.struct[5] = [list(x) for x in zip(*cube.struct[5])][::-1]
    else:
        print("ERROR the desired row is not possible in the given cube structure ")
        return


def vertical(cube, column , direction ):
    if column < len(cube.struct[o]):
        for i in range(len(cube.struct[0])):
            if direction == 0:
                cube.struct[0][i][column],cube.struct[2][i][column],cube.struct[4][-i-1][-column-1],cube.struct[5][i][column] = (cube.struct[4][-i-1][-column-1]cube.struct[0][i][column]cube.struct[5][i][column]cube.struct[2][i][column])
            if direction == 1:
                cube.struct[0][i][column],cube.struct[2][i][column],cube.struct[4][-i-1][-column-1],cube.struct[5][i][column] = (cube.struct[2][i][column],cube.struct[5][i][column],cube.struct[0][i][column],cube.struct[4][-i-1][-column-1])
            else:
                print("Error Direction is not possible")
                return 
        if direction == 0:
            if column == 0:
                cube.struct[1] = [list(x) for x in zip(*cube.struct[1])][::-1]
            elif column == len(cube.struct[0])-1:
                cube.struct[3] =  [list(x) for x in zip(*cube.struct[3])][::-1]
        elif direction == 1:
            if column == 0:
                cube.struct[1] = [list(x) for x in zip(*reversed(cube.struct[1]))]
            elif column == len(cube.struct[0])-1:
                cube.struct[3] = [list(x) for x in zip(*reversed(cube.struct[3]))]
    else:
        print("ERROR column no is out of bound for the structure ")
        return 

