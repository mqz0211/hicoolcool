import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


WHITE  = (255, 255, 255)
BLUE   = (0, 100, 255)
BLACK  = (0, 0, 0)
BORDER_COLOR = (200, 0, 0) # Red border

SPEED = 5

class Player:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 50, 50)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]: self.rect.x -= SPEED
        if keys[pygame.K_d]: self.rect.x += SPEED
        if keys[pygame.K_w]: self.rect.y -= SPEED
        if keys[pygame.K_s]: self.rect.y += SPEED

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("hicoolcool")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Comic sans", 24)
    tag_surface = font.render("mqz ma niga", True, BLACK)
    tag_rect = tag_surface.get_rect(bottomright=(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 10))

    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.handle_input()

        screen.fill(WHITE)

        pygame.draw.rect(screen, BORDER_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
        
        player.draw(screen)
        screen.blit(tag_surface, tag_rect)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
