# from builtins import input
#
# print('how you name')
# name = input()
# print("Hi", name)

# name = input("как тебя зовут?")
# print("Пирвет!", name)
# x1 = 100
# #b = True
# while x1 < 0:#True:
#     #if x1 < 0:
#     #    break
#     print(x1)
#     x1 -= 1
# #print("finish")

# for x in range(0,100,10):
#     print(x)
# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(1)
# elif x > 0 and y < 0:
#     print(4)
# else:
#     print("never")

# import turtle
#
# turtle.shapesize(2)
# turtle.forward(100)
# #turtle.shape('turtle')
# def turt1():
#
#     x = 1
#     for step in range(100):
#         turtle.forward(99)
#         turtle.right(101)
#         turtle.speed(x)
#         x +=x
#        # print(step)
#
# turt1()
# turtle.backward(300)
# turt1()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x ** 2)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
plt.show()

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

ax = axes3d.Axes3D(plt.figure())
i = np.arange(-10, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X ** 2 - Y ** 2
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
plt.show()

import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy


def makeData():
    x = numpy.arange(-10, 10, 1)
    y = numpy.arange(-10, 10, 1)
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = numpy.sin(xgrid) * numpy.sin(ygrid) / (xgrid * ygrid)
    return xgrid, ygrid, zgrid


x, y, z = makeData()

fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.jet)
pylab.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x ** 2)
plt.show()

import turtle

turtle.shapesize(2)
turtle.forward(100)
# turtle.shape('turtle')
x = 1
for step in range(1000):
    turtle.forward(1+x)

    # turtle.backward(100)
    turtle.right(1+1.1 *x)
    turtle.speed(1000)
    x += 1


def hello(name):
    print('Hello, ', name,'!')

hello('world')


import turtle
turtle.shapesize(2)
# turtle.shape('turtle')
def r(stepX):

    for step in range(stepX):
        turtle.forward(stepX)

        # turtle.backward(100)
        turtle.right(360/stepX)
        turtle.speed(100)
   # print(stepX)
    stepX -= 1
    turtle.right(90)
    turtle.forward(360/stepX)
    turtle.right(-90)

    if stepX > 0:
        r(stepX)

r(10)


import turtle
turtle.color('black', 'yellow')

turtle.shapesize(2)

x = 361
turtle.speed(10000)
for step in range(x):
    turtle.right(1)
    turtle.forward(2)
    if step % 2:
        turtle.hideturtle()
    else:
        turtle.showturtle()


def foo() -> int:
    
#x2 = 2
y1 = "a" #input()
def foo1(b:str, a:int):
    for


    #return  b

print(y1)
foo1(y1)
print(y1)


def foo(x = 0, y = 0, z = 0):
    return 1000*x + 10*y + 1*z

'''
print(foo(z=1, y=2))
'''
def bar(*args, b='1'):
    for arg in args:
        print(arg)
    print(b)

bar(1,2, b=2)

# Import a library of functions called 'pygame'
import pygame
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [600, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draw on the screen a GREEN line from (0, 0) to (50, 30)
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)

    # Draw on the screen 3 BLACK lines, each 5 pixels wide.
    # The 'False' means the first and last points are not connected.
    pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

    # Draw on the screen a GREEN line from (0, 50) to (50, 80)
    # Because it is an antialiased line, it is 1 pixel wide.
    pygame.draw.aaline(screen, GREEN, [0, 50], [50, 80], True)

    # Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)

    # Draw a solid rectangle
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    # Draw a rectangle with rounded corners
    pygame.draw.rect(screen, GREEN, [115, 210, 70, 40], 10, border_radius=15)
    pygame.draw.rect(screen, RED, [135, 260, 50, 30], 0, border_radius=10, border_top_left_radius=0,
                     border_bottom_right_radius=15)

    # Draw an ellipse outline, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)

    # Draw an solid ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)

    # Draw a circle
    pygame.draw.circle(screen, BLUE, [60, 250], 40)

    # Draw only one circle quadrant
    pygame.draw.circle(screen, BLUE, [250, 250], 40, 0, draw_top_right=True)
    pygame.draw.circle(screen, RED, [250, 250], 40, 30, draw_top_left=True)
    pygame.draw.circle(screen, GREEN, [250, 250], 40, 20, draw_bottom_left=True)
    pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()

