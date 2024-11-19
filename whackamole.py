import pygame
import random



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_position = (0,0)
        square_size = 32
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_x, mole_y = mole_position
                    if mole_x<= mouse_x < mole_x + square_size and mole_y <=mouse_y < mole_y + square_size:
                        mole_position = (
                            random.randrange(0,640, square_size),
                            random.randrange(0, 512, square_size))

            screen.fill("light green")
            for i in range(0, 641, 32):
                pygame.draw.line(screen, "dark blue", (i, 0), (i, 512))
            for j in range(0, 513, 32):
                pygame.draw.line(screen, "dark blue", (0, j), (640, j))
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

