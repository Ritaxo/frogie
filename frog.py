# Authors: Jada Baldoza and Amrita
# Find your way home without being eaten

import pygame
import random
import math

pygame.init()

size = [800, 600]  #size of game window
gameWindow = pygame.display.set_mode(size)
pygame.display.set_caption('Let Us Find and Save Nemo')

#RGB colors
Black = (0,0,0) # the lack of color
White = (255,255,255) # the presence of color
Red = (255, 0,0)
Green = (187,255,153)
Blue= (240,248,255)

clock = pygame.time.Clock()

# Load marlon, nemo and other character images.
marlon = pygame.image.load('images_pygame/marlon.jpg')
n1 = pygame.image.load('images_pygame/nemo.jpeg')
n2 = pygame.image.load('images_pygame/nemo.jpeg')
n3 = pygame.image.load('images_pygame/nemo.jpeg')
home = pygame.image.load('images_pygame/home.jpg') # Home picture 

# Predators: Sharks images
bruce = pygame.image.load('images_pygame/bruce.png')
anchor = pygame.image.load('images_pygame/anchor.jpeg')
mako = pygame.image.load('images_pygame/mako.png')

# Change their size
OtherSize = [70, 50]
marlon = pygame.transform.scale(marlon, OtherSize)
bruce = pygame.transform.scale(bruce, OtherSize)
anchor = pygame.transform.scale(anchor, OtherSize)
mako = pygame.transform.scale(mako, OtherSize)
HomeSize = [100, 100]
home= pygame.transform.scale(home, HomeSize)

# change the size of nemo
NemoSize = [30, 30]
n1 = pygame.transform.scale(n1, NemoSize)
n2 = pygame.transform.scale(n2, NemoSize)
n3 = pygame.transform.scale(n3, NemoSize)

# Function to display the Sprites in the game
def display_img(x, y, x_n1, y_n1, x_n2, y_n2, x_n3, y_n3,x_n4,y_n4, n1_alive, n2_alive, n3_alive, xb, yb, xa, ya, xm, ym, marlon_alive, home_alive, home):
    if marlon_alive:
        gameWindow.blit(marlon, (x,y))  # (0,0) is upper left

    gameWindow.blit(bruce, (xb,yb))
    gameWindow.blit(anchor, (xa,ya))
    gameWindow.blit(mako, (xm,ym))
    gameWindow.blit(home, (x_n4,y_n4)) # home coordinate
    
   
    if n1_alive:  #nemo's coordinates when alive
        gameWindow.blit(n1, (x_n1, y_n1))
    if n2_alive:
        gameWindow.blit(n1, (x_n2, y_n2))
    if n3_alive:
        gameWindow.blit(n1, (x_n3, y_n3))
    if home_alive:
        gameWindow.blit(home, (x_n4, y_n4))
        
def hit_walls(x, y, xmin, xmax, ymin, ymax):
    # If img hits the boundaries, wrap around
    if x > xmax:
        x = xmin
    elif x < xmin:
        x = xmax
    if y > ymax:
        y = ymin
    elif y < ymin:
        y = ymax
    return(x,y)

def m_hit_walls(x, y, xmin, xmax, ymin, ymax):
    # keep nemo inside boundaries since its trap with the sharks
    q = 40
    if x > xmax:
        x = xmax - q
    elif x < xmin:
        x = xmin + q
    if y > ymax:
        y = ymax - q
    elif y < ymin:
        y = ymin + q
    return(x,y)

def follow(x, y, xc, yc, alive):
    # d is the distance between the marlon and the predators
    d = math.sqrt((x -xc) **2 ) + (( y - yc) ** 2)
    if (d < 15):
        alive = False   # marlon has been eaten
        
    if ((random.randint(1, 100)) < 80) and (d < 200):
        p1 = x - xc
        p2 = y - yc
        xc +=  (p1 / 5)
        yc +=  (p2 / 5)
        return(xc, yc, alive)
    else:
        return(xc, yc, alive)
    
def set_obj_position(x, y, xnew, ynew):
    # x and y are the positions of the object with the directions applied
    return x, y, xnew, ynew
def set_position(x, y):
    # x and y are the set positions of the object
    return x, y
    
def game():
    # x and y are the positions of the marlon
    x, y, new_x, new_y = set_obj_position(20, 20, 0, 0)
    # position of nemo 1
    x_n1, y_n1, new_x_n1, new_y_n1 = set_obj_position(300, 300, 0, 0)
    # position of nemo 2
    x_n2, y_n2, new_x_n2, new_y_n2 = set_obj_position(400, 600, 0, 0)
    # position of nemo 3
    x_n3, y_n3, new_x_n3, new_y_n3 = set_obj_position(700, 100, 0, 0)
    # position of the sharks
    xb, yb = set_position(200, 260)
    xa, ya = set_position(550, 450)
    xm, ym = set_position(400, 380)
    x_n4, y_n4 = set_position(600, 500) #Home where Marlon needs to go in the end

    end = False
    n1_alive = True
    n2_alive = True
    n3_alive = True
    home_alive= True
    marlon_alive = True

    while not end:

        # event handler loop
        for event in pygame.event.get(): # gets user events
            if event.type == pygame.QUIT:  # click x
                     end = True
                     print(event) # prints to console
            if event.type == pygame.KEYDOWN:  # pressing key down
                if event.key == pygame.K_LEFT:   #left arrow key
                    new_x = -5 # move our image to the left
                elif event.key == pygame.K_RIGHT:
                    new_x = 5
                elif event.key == pygame.K_UP:
                    new_y = -5
                elif event.key == pygame.K_DOWN:
                    new_y = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    new_x = 0  #  stop image from moving in the x direction
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    new_y = 0  #  stop image from moving in the y direction

        # nemo move randomly inside the rectangle waiting to be saved
        z = 10
        x_n1 += random.randint(-z, z)
        y_n1 += random.randint(-z, z)
        x_n2 += random.randint(-z, z)
        y_n2 += random.randint(-z, z)
        x_n3 += random.randint(-z, z)
        y_n3 += random.randint(-z, z)

         # If nemos hits the boundaries, stop them from leaving area
        (x_n1,y_n1) = m_hit_walls(x_n1, y_n1,100, 300, 100, 300)
        (x_n2,y_n2) = m_hit_walls(x_n2, y_n2,200, 400, 400, 600)
        (x_n3,y_n3) = m_hit_walls(x_n3, y_n3,500, 700, 0, 200)

        # Display background before the new location of the image
        gameWindow.fill(Blue)

        if marlon_alive:  # Calculate the new location
            x += new_x
            y += new_y
            
        if marlon_alive: # distance between marlon and nemo
            d1 = math.sqrt( (x - x_n1)**2 + (y - y_n1)**2 )
            d2 = math.sqrt( (x - x_n2)**2 + (y - y_n2)**2 )
            d3 = math.sqrt( (x - x_n3)**2 + (y - y_n3)**2 )
            # distance between marlon and home
            d4 = math.sqrt( (x - x_n4)**2 + (y - y_n4)**2 )

            # Simulate marlon saving nemos and getting home
            d = 5
            if (d1 < d):
                n1_alive =  False
            if (d2 < d):
                n2_alive =  False
            if (d3 < d):
                n3_alive =  False
            if (d4 < 20):
                home_alive = False 
                
            
            # Simulate the sharks following the marlon and maybe eating the marlon
            marlon_alive = True
            xb, yb, marlon_alive = follow(x, y, xb, yb, marlon_alive)
            xa, ya, marlon_alive = follow(x, y, xa, ya, marlon_alive)
            xm, ym, marlon_alive = follow(x, y, xm, ym, marlon_alive)

            # If marlon hits the boundaries, wrap around
            (x,y) = hit_walls(x, y, 0, size[0], 0, size[1])
            

        # If predators hit the boundaries, stop them from leaving area
        (xb,yb) = m_hit_walls(xb, yb, 100, 300, 100, 300)
        (xa,ya) = m_hit_walls(xa, ya, 200, 400, 400, 600)
        (xm,ym) = m_hit_walls(xm, ym, 500, 700, 0, 200)

        # Display all the creatures
        display_img(x, y, x_n1, y_n1, x_n2, y_n2, x_n3, y_n3,x_n4, y_n4, n1_alive, n2_alive, n3_alive, xb, yb, xa, ya, xm, ym, marlon_alive, home_alive,home)

        # Game instructions 
        fontObj = pygame.font.Font('freesansbold.ttf', 15)
        textSurfaceObj = fontObj.render('Save All Nemos from Sharks', True, Black, White)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (300, 30)
        gameWindow.blit(textSurfaceObj, textRectObj)

        fontObj = pygame.font.Font('freesansbold.ttf', 15)
        textSurfaceObj = fontObj.render('Move Arrow to Save Nemo Then Go Home', True, Black, White)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (300, 45)
        gameWindow.blit(textSurfaceObj, textRectObj)

        if (not marlon_alive):
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('You Lost and Nemos were not Saved :(', True, Green, Blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (400, 150)
            gameWindow.blit(textSurfaceObj, textRectObj)

        elif (not n1_alive) and (not n2_alive) and (not n3_alive) and (not home_alive):
          
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('YOU WON!.', True, Green, Blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (400, 150)
            gameWindow.blit(textSurfaceObj, textRectObj)

        # Now we are ready to display all the work done
        pygame.display.update()

        # FPS Frames Per Second, how fast things move
        clock.tick(60)

# Here we start the game by calling the main function game()
game()
pygame.quit()


