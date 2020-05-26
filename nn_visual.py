"""
A visualization of linearly seperable classification using
a Perceptron class I wrote. I use pygame here. 
But matplotlib would work.
"""


import pygame, sys
from random import randint
# Uses perceptron class in repository
from perceptron import Perceptron

# Create a point class to use in viual and training
class Point:

    # Initialize a x and y value for coordinate and label for training
    # Color is for other projects
    def __init__(self,x,y):
        self.x = x
        self.y = y

        if x > y:
            self.label = 1
        else:
            self.label = 0

        self.color = " "

    # method to show point in pygame.
    def show(self):
        self.rect = pygame.Rect(self.x,self.y,20,20)
        pygame.draw.ellipse(window,self.color,self.rect)



# Initialize a new instance of the Percetron class as "brain"
brain = Perceptron(2)

pygame.init()

size = width, height = 500,500

window = pygame.display.set_mode(size)

run = True

# Initialize empty points list
points = []

# fill points list
for i in range(100):
    p = Point(randint(0,width-20),randint(0,height-20))
    points.append(p)

# train brain on points a certain number of times
for i in range(1000):
    for point in points:
        brain.train([point.x,point.y],point.label)

# Create a test point for testing after training

# set attributes for asthetics and initaite point class

guess_point = Point(randint(0,width),randint(0,height))
guess_point.color = (0,255,0)

window.fill((255,255,255))

font = pygame.font.SysFont("Comic Sans",28)

 
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            # sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass



    pygame.draw.line(window,(0,0,0),(0,0),(width,height),2)

    img = font.render("The result should be: {}".format(guess_point.label),True,(0,0,0))
    window.blit(img,(280,20))


    # Show the test point
    guess_point.show()

    pygame.display.update()

# Make a guess on test point shown in pygame window after quitting
print(brain.guess([guess_point.x,guess_point.y]))