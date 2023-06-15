from pygame import *

finish = True
win_widht = 700
win_height = 500
game = True
clock = time.Clock()
FPS = 60
# Создание игрового окна
window = display.set_mode((win_widht, win_height))
display.set_caption("Шутер")
background = transform.scale(image.load('valera.png'), (win_widht, win_height))
font.init()
font1 = font.SysFont('Arial',80)
win = font1.render('YOU WIN',True,(200,200,100))
lose = font1.render('YOU LOSE', True,(200,200,100))


# Сделать пременные отвечающие за написание на экране надписей
# Основной класс
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,player_speed_y):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.speed_y = player_speed_y

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# Класс платформы (Игрока)
class Platphorm(GameSprite):
    # Функция обновления обьекта
    # Управление через WASD
    def update_wasd(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    # Управление через стрелочки
    def update_arrow(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


# Класс мяча
class Ball(GameSprite):
    # Функция обновления обьекта
    def update(self):
        self.rect.x -= self.speed
        self.rect.y -= self.speed_y

        if self.rect.x <0 or self.rect.x > win_widht:
            finish = False
        
        if self.rect.y < 0 or self.rect.y > win_height:
            self.speed *=-1
            self.speed_y *= -1
        
        if sprite.collide_rect(self,player_wasd) or sprite.collide_rect(self,player_arrow):
            self.speed *= -1
            self.speed_y *= -1

# Экземпляры классов
player_wasd = Platphorm('platform.png', 10, 200, 65, 80, 10,0)
player_arrow = Platphorm('platform.png', 630, 200, 65, 80, 10,0)
ball = Ball('ball.png', 400, 200, 65, 80, 10,1)
# Игровой цикл
while game:
    # Сделать завешение игры по нажатию крестика
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        window.blit(background, (0, 0))
    # Реализовать отрисовку спрайтов мяча и платформ
    player_wasd.update_wasd()
    player_wasd.reset()

    player_arrow.update_arrow()
    player_arrow.reset()

    ball.update()
    ball.reset()
    if ball.rect.x <0 or ball.rect.x > win_widht-80:
        window.blit(lose,(170,170))
        finish = False
    # Проверка взаимодействия обьектов
    display.update()
    time.delay(FPS)