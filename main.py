import random
import pygame

window_height = 800
window_width = 1000
snake_size = 20
snake_direction = ''
snake_list = []
length_snake = 1
food_x = random.randint(0, (window_width / snake_size) - 1) * snake_size 
food_y = random.randint(0, (window_height / snake_size) - 1) * snake_size
x1 = 0
y1 = 0
 
x1_change = 0       
y1_change = 0

particles = []

def draw_particles(obj: object) :
    obj["x"] += obj["vx"]
    obj["y"] += obj["vy"]
    obj["size"] -= 0.3
    obj["vy"] += 1.5
    pygame.draw.rect(screen, (124, 252, 0), (obj["x"], obj["y"], obj["size"], obj["size"]))

def draw(amount, x, y):
    for i in range(amount):
        obj = {
            "size": random.randint(2, 6),
            "x": x,
            "y": y,
            "vx": random.randint(-5, 20),
            "vy": random.randint(-5, 20)
        }
        particles.append(obj)

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")
pygame.init()

while True:
    flag = False
    pygame.time.delay(100)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    key_press = pygame.key.get_pressed()

    if key_press[pygame.K_l]:
        length_snake += 10

    if key_press[pygame.K_w] and snake_direction != "down":
        snake_direction = "up"
        y1_change = -snake_size
        x1_change = 0
    elif key_press[pygame.K_s] and snake_direction != "up":
        snake_direction = "down"
        y1_change = snake_size
        x1_change = 0
    elif key_press[pygame.K_d] and snake_direction != "left":
        snake_direction = "right"
        x1_change = snake_size
        y1_change = 0
    elif key_press[pygame.K_a] and snake_direction != "right":
        snake_direction = "left"
        x1_change = -snake_size
        y1_change = 0


    x1 += x1_change
    y1 += y1_change
 
    pygame.draw.rect(screen, (124, 252, 0), (food_x, food_y, snake_size, snake_size))
    if x1 > window_width - snake_size:
        x1 = 0
    elif y1 > window_height - snake_size:
        y1 = 0
    elif x1 < 0:
        x1 = window_width - snake_size
    elif y1 < 0:
        y1 = window_height - snake_size
    snake_head = [x1, y1]
    snake_list.append(snake_head)

    
    if x1 == food_x and y1 == food_y:
        draw(100, food_x, food_y)
        flag = True
        food_x = random.randint(0, (window_width / snake_size) - 1) * snake_size 
        food_y = random.randint(0, (window_height / snake_size) - 1) * snake_size
        length_snake += 1

    for i in particles:
        draw_particles(i)

    if len(snake_list) > length_snake:
        del snake_list[0]
    for idx, x in enumerate(snake_list):
        if idx == len(snake_list) - 1:
            pygame.draw.rect(screen, (255, 255, 255), (x[0], x[1], snake_size, snake_size))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (x[0], x[1], snake_size, snake_size))

    pygame.display.update() 