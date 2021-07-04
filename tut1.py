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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect.move_ip(0,-20)
            elif event.key == pygame.K_s:
                rect.move_ip(0,20)
            elif event.key == pygame.K_a:
                rect.move_ip(-20,0)
            elif event.key == pygame.K_d:
                rect.move_ip(20,0)

    screen.fill(BLACK)
    screen.blit(image,rect)
    pygame.display.update()



