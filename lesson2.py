import pygame

# Initialize the pygame
pygame.init()

# Create the screen , width and height
screen = pygame.display.set_mode((500, 500))

#creating another variable for the screen width
screenWidth = 500

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# setting variables for screem
x = 50
y = 50
width = 40
height = 60
vel = 5

# actions
isJump = False
jumpCount = 10

# Set Title and Icon
pygame.display.set_caption("Test")

icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# Game Loop
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenWidth - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount > -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -=  (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
    

    screen.fill(black)
    pygame.draw.rect(screen, red, (x, y, width, height))
    pygame.display.update() 

pygame.quit()
quit()




