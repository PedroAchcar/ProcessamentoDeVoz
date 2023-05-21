import pygame


def display_meaning(meaning: list):
    pygame.init()

    width = 1300
    height = 500
    font_size = 36
    vertical_space = 10

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('DiciVoz')

    white = (255, 255, 255)
    black = (0, 0, 0)

    font = pygame.font.Font(None, font_size)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(black)

        vertical = height // 2 - \
            ((font_size + vertical_space) * len(meaning)) // 2

        for phrase in meaning:
            surface_text = font.render(phrase, True, white)
            horizontal = width // 2 - surface_text.get_width() // 2
            screen.blit(surface_text, (horizontal, vertical))
            vertical += font_size + vertical_space

        pygame.display.flip()

    pygame.quit()
