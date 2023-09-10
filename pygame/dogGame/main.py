from random import randint
import pygame
pygame.init()

DOG_NORMAL_VELOCITY = 5
DOG_BOOST_VELOCITY = 10
PLAYER_STARTING_BOOSTLEVEL = 100
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
dog_velocity = DOG_NORMAL_VELOCITY
boost_level = PLAYER_STARTING_BOOSTLEVEL
BURGER_STARTING_VELOCITY = 4
burger_velocity = BURGER_STARTING_VELOCITY


score = 0
burger_points = 0


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

dog_left = pygame.image.load("dog.png")
dog_right = pygame.transform.flip(dog_left, True, False)

font = pygame.font.Font("Franxurter.ttf", 24)
boost_text = font.render(f"boost level: {boost_level}", True, (234, 10, 217))
boost_rect = boost_text.get_rect(topleft=(5, 5))
score_text = font.render(f"score: {score}", True, (234, 10, 217))
score_rect = score_text.get_rect(topleft=(5, 35))
burger_points_text = font.render(
    f"burger_points: {burger_points}", True, (234, 10, 217))
burger_points_rect = burger_points_text.get_rect(
    topright=(WINDOW_WIDTH - 25, 35))

dog = dog_left
dog_rect = dog.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-32))


burger = pygame.image.load("burger.png")
burger_rect = burger.get_rect()
burger_rect.topleft = (randint(0, WINDOW_WIDTH - 32), -100)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dog_rect.top > 0:
        dog_rect.y -= dog_velocity
    if keys[pygame.K_DOWN] and dog_rect.bottom < WINDOW_HEIGHT:
        dog_rect.y += dog_velocity
    if keys[pygame.K_LEFT] and dog_rect.left > 0:
        dog = dog_left
        dog_rect.x -= dog_velocity
    if keys[pygame.K_RIGHT] and dog_rect.right < WINDOW_WIDTH:
        dog = dog_right
        dog_rect.x += dog_velocity
    if keys[pygame.K_SPACE] and boost_level > 0:
        dog_velocity = DOG_BOOST_VELOCITY
        boost_level -= 1
    else:
        dog_velocity = DOG_NORMAL_VELOCITY

    burger_rect.y += burger_velocity

    if burger_rect.bottom >= WINDOW_HEIGHT:
        burger_rect.topleft = (randint(0, WINDOW_WIDTH - 32), -100)

    if dog_rect.colliderect(burger_rect):
        score += burger_points
        burger_rect.topleft = (randint(0, WINDOW_WIDTH - 32), -100)
        if boost_level < PLAYER_STARTING_BOOSTLEVEL:
            boost_level += 10

    burger_points = int((WINDOW_HEIGHT -burger_rect.y)/100)   + 1


    boost_text = font.render(
        f"boost level: {boost_level}", True, (234, 10, 217))
    score_text = font.render(f"score: {score}", True, (234, 10, 217))
    burger_points_text = font.render(
        f"burger_points: {burger_points}", True, (234, 10, 217))

    display_surface.fill((0, 0, 0))
    display_surface.blit(dog, dog_rect)
    display_surface.blit(boost_text, boost_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(burger, burger_rect)
    display_surface.blit(burger_points_text, burger_points_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
