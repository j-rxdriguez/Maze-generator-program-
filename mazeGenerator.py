# Here I'm importing libraries and modules that will be required for this program to run.
import pygame
import time
import random


# Setting up the frames for pygame window and its size
WIDTH = 450
HEIGHT = 450
FPS = 60
# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()


# Colours that I'll use
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)


# setup maze variables
w = 20                   # Cell's width which is 20 pixels wide
x = 0                    # X Axis
y = 0                    # Y Axis
grid = []
visited = []
stack = [] #For when the program gets stuck
solution = {} #Dictionary

# This code will start shaping the maze by building the grid.
def grid_builder(x, y, w):
    for i in range(1,21):


        #Here, X Coordinate its set as the starting position.
        x = 20                 
        #And Y is used to start a new row                                          
        y = y + 20                                                       
        for j in range(1, 21):
            #Each cell has a left, right , top and bottom.
            #Top of cell
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])      
            #Right of cell     
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   
            #Bottom of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   
             #Left of the cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])          
            # Next line adds a cell to the grid list
            grid.append((x,y))                                          
            # Next line moves the cell to a new position  
            x = x + 20                                                    

def move_up(x, y):
    #Creates an animation to show the walls being removed.
    pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1, 19, 39), 0)     
    pygame.display.update()                                              

def move_down(x, y):
    pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()

def move_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()

def move_right(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 39, 19), 0)
    pygame.display.update()

def cell1( x, y):
    #This code will draw a single width cell
    pygame.draw.rect(screen, GREEN, (x +1, y +1, 18, 18), 0)          
    pygame.display.update()

def retrn_cell(x, y):
    #Changes the colour of the path after the cells has been visited
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 18, 18), 0)        
    pygame.display.update()                                        

def cell_solve(x,y):
    #This code its used to show the solution
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0) 
    #Visited cells            
    pygame.display.update()                                        

def maze_paths(x,y):
    #Checks to seee if there are any cells to the left, right top or bottom that haven't been visited yet.

    cell1(x, y)   
    # X and Y are the starting positions for this maze
    # Starting cells are added to the stack
    stack.append((x,y))        
    #Starting cell is then added to the visited list.
    visited.append((x,y))      
    #Will loop until the stack is empty                                    
    while len(stack) > 0:  
    #Slow program down                                        
        time.sleep(.07)          
#Defines cell list                     
        cell = []                                   
        #If cell to the right is available tehn proceed to add it to cell list               
        if (x + w, y) not in visited and (x + w, y) in grid:       
            cell.append("right")                                   
#If left cell available append to cell list
        if (x - w, y) not in visited and (x - w, y) in grid:      
            cell.append("left")
#If down cell available append to cell list
        if (x , y + w) not in visited and (x , y + w) in grid:     
            cell.append("down")
#If up cell available append to cell list
        if (x, y - w) not in visited and (x , y - w) in grid:     
            cell.append("up")
#Check inside cell list to see if it is empty
        if len(cell) > 0:                                   
#Picks a random cell       
            selected_cell = (random.choice(cell))                    
#If the selected cell has been chosen then proceeed to call move_right function
            if selected_cell == "right":                       
                move_right(x, y)          
            # solution = dictionary key = new cell, other = current cell                      
                solution[(x + w, y)] = x, y        
                #Cell in use                
                x = x + w            
                #Append to list of visited                              
                visited.append((x, y))                  
                #Add current cell to stack           
                stack.append((x, y))                               

            elif selected_cell == "left":
                move_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif selected_cell == "down":
                move_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif selected_cell == "up":
                move_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
#Here the programs checks for available cells and if none are found pops one from the stack. 
#Cell1 function is used to show the backtracking image
            x, y = stack.pop()                                   
            cell1(x, y)    
# Sets the speed of the program (slower)
            time.sleep(.05)                             
# Colour changes to greeen so the return path is identified.         
            retrn_cell(x, y) 
                              

# Grid starting position
x, y = 20, 20                     
# 1st argument = x value, 2nd argument = y value, 3rd argument = Width of cell
grid_builder(40, 0, 20)             
# Call maze builder function
maze_paths(x,y)               

#Pygame loops
running = True
while running:
    # Sets the right speed for the clock
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #Kill program
        if event.type == pygame.QUIT:
            running = False