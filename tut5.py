import pygame

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))
screen = pygame.display.set_mode((720, 480))  # Notice the tuple! It's not 2 arguments.
clock = pygame.time.Clock()
FPS = 60  # This variable will define how many frames we update per second.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
rect = pygame.Rect((0, 0), (32, 32))  # First tuple is position, second is size.
image = pygame.Surface((32, 32))  # The tuple represent size.
image.fill(WHITE)  # We fill our surface with a nice white color (by default black).


while True:
    clock.tick(FPS)
    pygame.event.pump()  # Allow pygame to handle internal actions.
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_pos[0] > 100:
        pygame.mouse.set_pos(10, mouse_pos[1])  # Reset the mouse's x-position to 10.
        print("YOU SHALL NOT PASS!")
    if mouse_buttons[2]:
        print("I'm right, right?")
    if mouse_buttons[0]:  # Press left mouse button to exit.
        print("Program left")
        quit()

    pygame.display.update()