class RubiksCube:
    def __init__(cube,n=3,colours=['w','o','g','r','b','y'] ,string= none ):
        if state is none:
            cube.n = n 
            cube.colours = colours
            cube.reset()
            
        else:
            cube.n = int((len(state)/6)**(0.5))
            cube.colours = []
            cube.struct = [[[]]]
            for i, s in enumarate(string):
                if s not in cube.colours:
                    cube.colours.append(s)
                cube.struct[-1][-1].append(s)
                if len(cube.struct[-1][-1]==cube.n and len(cube.struct[-1])<cube.n:
                    cube.struct[-1].append([])
                elif len(cube.struct[-1][-1]) == cube.n and len (cube.struct[-1]) == cube.n and i<len(string)-1:
                    cube.struct.append([[]])

    def reset(cube):
        cube.struct = [[[c for x in range(cube.n)] for y in range(cube.n)] for c in cube.colours]




