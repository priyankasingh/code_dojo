import random

def maze_printer (maze):
    for row in maze:
        for column in row:
            if column: #true = WALL
                print "#",
            else:
                print " ",
                
        print "\n",

def maze_creator(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            maze[i][j] = True
            # maze[i][j] = (i == 0 or i == len(maze) - 1 or j == 0 or j == len(row) - 1)
            
    # x = 0
    # y = random.randint(1, len(maze[0]) - 2)
    # length = 0
    # minlength = 10
    
    # while length < minlength:
    #     maze[x][y] = False
        
    #     choice = random.choice([1, 2, 3, 4])
        
    #     if   choice == 1 and y > 0 and not maze[x][y-1]:
    #         y = y - 1
    #     elif choice == 2 and x < len(maze) - 1 and not maze[x+1][y]:
    #         x = x + 1
    #     elif choice == 3 and y < len(maze[0]) - 1 and not maze[x][y+1]:
    #         y = y + 1
    #     elif choice == 4 and x > 0 and not maze[x-1][y]:
    #         x = x - 1
        
    #     length = length + 1
            
    return maze

size = raw_input("Pick a maze size: ")
maze = [[True for a in range(int(size))] for b in range(int(size))]
maze = maze_creator(maze)
# maze = maze_algo(maze, 0, random.randint(1, len(maze[0]) - 2), "south")

maze_printer(maze)

visited = []
visited.append((0,0))
accumulator_maze = maze

def check_if_visited(tup):
    if tup in visited:
        return True
    else:
        return False

def maze_algo (array, nodeX, nodeY, directionTaken):
    
        
    array[nodeX][nodeY] = True
    if directionTaken == "left" :
            
            
        array[nodeX+1][nodeY]= False
        array[nodeX][nodeY-1]= False
        array[nodeX][nodeY+1]= random.choice([True, False])
        visited.append((nodeX+1,nodeY))
        visited.append((nodeX,nodeY-1))
        visited.append((nodeX,nodeY+1))
        if not check_if_visited((nodeX+1,nodeY)):
            maze_algo(array,nodeX+1,nodeY,"right")
        if not check_if_visited((nodeX,nodeY-1)):    
            maze_algo(array,nodeX,nodeY-1,"up")
        if not check_if_visited((nodeX,nodeY+1)):
            maze_algo(array,nodeX,nodeY+1,"down")
    elif directionTaken == "right":
        array[nodeX-1][nodeY]= False
        array[nodeX][nodeY-1]= random.choice([True, False])
        array[nodeX][nodeY+1]= False
        visited.append((nodeX-1,nodeY))
        visited.append((nodeX,nodeY-1))
        visited.append((nodeX,nodeY+1))
        if not check_if_visited((nodeX-1,nodeY)):
            maze_algo(array,nodeX-1,nodeY,"left")
        if not check_if_visited((nodeX,nodeY-1)):    
            maze_algo(array,nodeX,nodeY-1,"up")
        if not check_if_visited((nodeX,nodeY+1)):
            maze_algo(array,nodeX,nodeY+1,"down")
    elif directionTaken == "up":
        array[nodeX+1][nodeY]= False
        array[nodeX-1][nodeY]= random.choice([True, False])
        array[nodeX][nodeY+1]= False
        visited.append((nodeX+1,nodeY))
        visited.append((nodeX-1,nodeY))
        visited.append((nodeX,nodeY+1))
        if not check_if_visited((nodeX+1,nodeY)):
            maze_algo(array,nodeX+1,nodeY,"right")
        if not check_if_visited((nodeX-1,nodeY)):    
            maze_algo(array,nodeX-1,nodeY,"left")
        if not check_if_visited((nodeX,nodeY+1)):
            maze_algo(array,nodeX,nodeY+1,"down")
    else:
        array[nodeX+1][nodeY]= random.choice([True, False])
        array[nodeX][nodeY-1]= False
        array[nodeX-1][nodeY]= False
        visited.append((nodeX+1,nodeY))
        visited.append((nodeX,nodeY-1))
        visited.append((nodeX-1,nodeY))
        if not check_if_visited((nodeX+1,nodeY)):
            maze_algo(array,nodeX+1,nodeY,"right")
        if not check_if_visited((nodeX,nodeY-1)):    
            maze_algo(array,nodeX,nodeY-1,"up")
        if not check_if_visited((nodeX-1,nodeY-1)):
            maze_algo(array,nodeX-1,nodeY-1,"left")
        
    return;

maze_algo(maze,0,1,"right")
maze_printer(maze)