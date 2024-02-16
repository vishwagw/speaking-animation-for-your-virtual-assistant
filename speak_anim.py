
pygame.init()  
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ELSA speaking animation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_mouth(x, y, width, height):
    pygame.draw.ellipse(screen, BLACK, (x, y, width, height))

def speak_animation():
    for i in range(10):
        mouth_width = 50 + i*5
        mouth_height = 30 + i*2
        draw_mouth(375, 300, mouth_width, mouth_height)
        pygame.display.update()
        time.sleep(0.1)
        screen.fill(WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    speak_animation()
    pygame.display.update()

pygame.quit()

speak_animation()