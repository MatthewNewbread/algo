import pygame 

pygame.init()

class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.fill_color = color
    def set_color(self, color):
        self.fill_color = color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outline(self, color, size):
        pygame.draw.rect(window, color, self.rect, size)

class Picture(Area):
    def __init__(self, filename, x, y, width, height, color):
        Area.__init__(self, x, y, width, height, color)
        self.image = pygame.image.load(filename)
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Константы
SIZE = (500, 500)
BLUE = (200, 255, 255)
FPS = 40
ROW_ENEMY = 3
WIDHT_ENEMY = 50
HEIGHT_ENEMY = 50
WIDHT_BALL = 60
HEIGHT_BALL = 60
WIDHT_PLATFORM = 140
HEIGHT_PLATFORM = 50

# Переменные
game = True
count_enemy = 9
start_x = 0
start_y = 0

# Структура
enemys = list()

window = pygame.display.set_mode(SIZE)
window.fill(BLUE)
clock = pygame.time.Clock()

for i in range(ROW_ENEMY):
    x = start_x + (i * 27.5)
    y = start_y + (i * 55)
    for j in range(count_enemy):
        enemy = Picture("images.jpeg", x, y, WIDHT_ENEMY, HEIGHT_ENEMY, BLUE)
        enemys.append(enemy)
        x += 55
    count_enemy -= 1

ball = Picture("ball.jpg", 200, 250, WIDHT_BALL, HEIGHT_BALL, BLUE)
platform = Picture("platform.png", 150, 400, WIDHT_PLATFORM, HEIGHT_PLATFORM, BLUE)

while game:
    pygame.display.update()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break
    
    for enemy in enemys:
        enemy.fill()
        enemy.draw()
    
    ball.fill()
    ball.draw()
    platform.fill()
    platform.draw()