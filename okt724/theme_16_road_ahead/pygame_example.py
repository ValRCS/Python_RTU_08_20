# let's make a simple pygame that moves a circle around on key press
# pygame is good for making 2D games - side scrollers, top down, etc.
try:
    import pygame
except ImportError:
    print("Pygame is not installed. Let's install it.")
    print("command line: pip install pygame")
# print pygame version
print(f"Pygame version: {pygame.version.ver}")
# documentation https://www.pygame.org/docs/

# now let's initialize pygame
pygame.init()

# let's define some colors
# we can use RGB values
# we can use 0-255 values
# or we can use pygame.Color
# let's use pygame.Color

# let's make a screen
screen = pygame.display.set_mode((800, 600))
# let's set the title
pygame.display.set_caption("Move the circle")

# let's make a clock
clock = pygame.time.Clock()

# let's make a circle
circle_x = 400
circle_y = 300
circle_radius = 50
circle_color = pygame.Color("red")
score = 0

# let's make a game loop
running = True
while running:
    # let's fill the screen with white color
    screen.fill(pygame.Color("white"))

    # let's draw the circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # show score in upper left corner
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, pygame.Color("black"))

    screen.blit(text, (10, 10))

    # let's update the screen
    pygame.display.flip()

    # let's limit the frame rate to 60 FPS - frames per second
    clock.tick(60)

    # let's handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # let's move the circle
        elif event.type == pygame.KEYDOWN:
            score += 1
            if event.key == pygame.K_LEFT:
                circle_x -= 10                
            elif event.key == pygame.K_RIGHT:
                circle_x += 10
            elif event.key == pygame.K_UP:
                circle_y -= 10
            elif event.key == pygame.K_DOWN:
                circle_y += 10

